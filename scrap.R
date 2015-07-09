rm(list=ls())

# Load libraries
library("XML")

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
    bls.store.info[i] = trim(trim.spaces(trim.html.chars(bls.store.info[i])))
  }
  if (grep("Address: ", bls.store.info[1])) {
    bls.store.info[1] = gsub("Address: ", "", bls.store.info[1])
  } else {
    print(paste("Address error at index:", 3))
  }
  if (grep("Phone:| Call", bls.store.info[2])) {
    bls.store.info[2] = gsub("Phone:| Call", "", bls.store.info[2])
  } else {
    print(paste("Phone error at index:", 3))
  }
  
  if (grep("Other information: ", bls.store.info[3])) {
    bls.store.info[3] = gsub("Other information: ", "", bls.store.info[3])
    bls.hours.list = unlist(strsplit(bls.store.info[3], "(?<=pm )", perl = TRUE))
    bls.hours.list = bls.hours.list[-length(bls.hours.list)]
    bls.hours.list = unlist(lapply(bls.hours.list, trim))
    bls.store.info[3] = paste(bls.hours.list, collapse = "|")
  } else {
    print(paste("Hours error at index:", 3))
  }
  store.data <- rbind(store.data, t(bls.store.info))
}

# -----------------------------------------------------------------------------
# Data match
# -----------------------------------------------------------------------------
# data from BC Government and reformatted after latlon
data.file <- read.csv("liquor/static/data.csv")

# 200 BC Liquor Stores from the dataset
length(data.file[data.file$type == "BC Liquor Store",]$address)


