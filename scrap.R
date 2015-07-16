rm(list=ls())

# Load libraries
library("XML")
library("geosphere")

# set to current working directory
setwd("~/git/3K1S")

# support functions
trim <- function(str) gsub("^\\s+|\\s+$", "", str)
trim.spaces <- function(str) gsub("\\s+", " ", str)
trim.html.chars <- function(str) gsub("\\n\\t", " ", str)

# -----------------------------------------------------------------------------
# Scrap data
# -----------------------------------------------------------------------------
# load BC Liquor Store website: http://m.bcliquorstores.com/m/stores/0
bls.url <- "http://m.bcliquorstores.com/m/stores/0"
bls <- xmlRoot(htmlTreeParse(bls.url, useInternalNodes = TRUE))
bls.parse <- xpathSApply(bls, "//a[@href]", xmlGetAttr, "href"); bls.parse

# load and format urls to visit
bls.urls <- lapply(bls.parse, function(x) if(length(grep("/m/stores/view", x) == TRUE)) x)
bls.urls <- unlist(bls.urls[!sapply(bls.urls, is.null)]); bls.urls
bls.urls <- unlist(lapply(bls.urls, function(x) unlist(strsplit(x, "/m/stores"))[2])); bls.urls
bls.urls <- unlist(lapply(bls.urls, function(x) paste(unlist(strsplit(bls.url, "/0")), x, sep = ""))); bls.urls
length(bls.urls)

# empty data frame
store.data <- data.frame(Address = character(), Phone = character(), Hours = character())

for (k in 1:length(bls.urls)) {
  print(paste("........................ ", format(round(k/length(bls.urls) * 100, 2), nsmall = 2), "%", sep=""))
  # load store information
  bls.store <- xmlRoot(htmlTreeParse(bls.urls[k], useInternalNodes = TRUE))#; bls.store
  bls.store.info <- xpathSApply(bls.store, "//div[@class='p10 clearfix']", xmlValue)[-1]#; bls.store.info
  
  # format information
  names(bls.store.info) <- c("Address", "Phone", "Hours")
  for (i in 1:length(bls.store.info)) {
    bls.store.info[i] <- trim(trim.spaces(trim.html.chars(bls.store.info[i])))
  }
  if (grepl("Address: ", bls.store.info[1])) {
    bls.store.info[1] <- gsub("Address: ", "", bls.store.info[1])
  } else {
    print(paste("Address error at index:", 3))
  }
  if (grepl("Phone:| Call", bls.store.info[2])) {
    bls.store.info[2] <- gsub("Phone:| Call", "", bls.store.info[2])
  } else {
    print(paste("Phone error at index:", 3))
  }
  
  if (grepl("Other information: ", bls.store.info[3])) {
    bls.store.info[3] <- gsub("Other information: ", "", bls.store.info[3])
    bls.hours.list <- unlist(strsplit(bls.store.info[3], "(?<=pm )", perl = TRUE))
    bls.hours.list <- bls.hours.list[-length(bls.hours.list)]
    bls.hours.list <- unlist(lapply(bls.hours.list, trim))
    bls.store.info[3] <- paste(bls.hours.list, collapse = "|")
  } else {
    print(paste("Hours error at index:", 3))
  }
  store.data <- rbind(store.data, t(bls.store.info))
}

# save as a csv for backup
write.csv(store.data, "liquor/static/scrapped.csv", row.names = FALSE)

# -----------------------------------------------------------------------------
# Add lat & lon information to scrapped data
# -----------------------------------------------------------------------------
store.data <- read.csv("liquor/static/scrapped.csv", header = TRUE)
google_api_address <- "https://maps.googleapis.com/maps/api/geocode/json?address="

# add columns to store.data
store.data$lat <- 0
store.data$lon <- 0

for (i in 1:nrow(store.data)) {
  request_url <- paste(google_api_address,
                      curlEscape(store.data$Address[i]), sep = "")
  response <- fromJSON(getURL(request_url))
  store.data[i,5] <- response$results[[1]]$geometry$location["lat"]
  store.data[i,6] <- response$results[[1]]$geometry$location["lng"]
  Sys.sleep(0.3)
  print(paste("........................ ", format(round(i/nrow(store.data) * 100, 2), nsmall = 2), "%", sep=""))
}

# save as a csv for backup
write.csv(store.data, "liquor/static/scrapped.csv", row.names = FALSE)

# -----------------------------------------------------------------------------
# Data match
# -----------------------------------------------------------------------------
# data from BC Government and reformatted after latlon
store.data <- read.csv("liquor/static/scrapped.csv", stringsAsFactors = FALSE)
data.file <- read.csv("liquor/static/data.csv", stringsAsFactors = FALSE)

class(data.file) == class(store.data)

# add hours & phone columns
data.file$hours <- ""
data.file$phone <- ""

# cross-match lat lons of two different datasets to determine their relationships
for (i in 1:nrow(data.file[data.file$type == "BC Liquor Store",])) {
  data.file.index <- as.numeric(rownames(data.file[data.file$type == "BC Liquor Store",][i,]))
  data.file.lat <- data.file[data.file.index,"lat"]
  data.file.lon <- data.file[data.file.index,"lon"]
  distances <- data.frame(lat1 = store.data$lat, lat2 = data.file.lat,
                          lon1 = store.data$lon, lon2 = data.file.lon,
                          distance = 0)
  haver.dist <- apply(distances[, c("lat1", "lat2", "lon1", "lon2")], 1,
                      function(x) distHaversine(c(x["lon1"], x["lat1"]), c(x["lon2"], x["lat2"])))

  store.data.index <- match(min(haver.dist), haver.dist)
  
  # add new information to data.file
  data.file$hours[data.file.index] <- store.data$Hours[store.data.index]
  data.file$phone[data.file.index] <- store.data$Phone[store.data.index]
}

write.csv(data.file, "liquor/static/data_hours_phone.csv", row.names = FALSE)


# -----------------------------------------------------------------------------
# Definitions of done:
# - (Government owned) BC liquor stores are correctly paired up with their hours of operation.
# - Private liquor stores’ hours of operation is null/not available
# -----------------------------------------------------------------------------
data.file <- read.csv("liquor/static/data_hours_phone.csv", stringsAsFactors = FALSE)

# the hours cell of BC Liquor Store should contain more than 0 character
# the hours cell of Private Liquor Store and others should contain 0 character
all(lapply(data.file[data.file$type == "BC Liquor Store",]$hours, function(x) nchar(x) > 0) == TRUE)
all(lapply(data.file[data.file$type == "Private Liquor Store",]$hours, function(x) nchar(x) == 0) == TRUE)
all(lapply(data.file[data.file$type == "Proposed Store Location",]$hours, function(x) nchar(x) == 0) == TRUE)

