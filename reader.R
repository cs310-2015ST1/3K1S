rm(list=ls())

library(RCurl)
library(rjson)

setwd("~/git")

google_api_address <- "https://maps.googleapis.com/maps/api/geocode/json?address="
data_file <- read.csv("http://www.pssg.gov.bc.ca/lclb/docs-forms/web_lrs.csv")

nrow(data_file[grep("BC Liquor Store", data_file$type, ignore.case=T),]) + 
nrow(data_file[grep("Private Liquor Store", data_file$type, ignore.case=T),]) + 
nrow(data_file[grep("Proposed Store Location", data_file$type, ignore.case=T),]) == nrow(data_file)

data_file$lat <- 0
data_file$lon <- 0

# address column does not have province information
parse_address <- function(city, address) return (paste(address, city, "BC", sep=", "))

for (i in 1:nrow(data_file)) {
  formatted_address = parse_address(data_file[i, 1], data_file[i, 3])
  request_url = paste(google_api_address,
                      curlEscape(formatted_address), sep="")
  print(request_url)
  response = fromJSON(getURL(request_url))
  data_file[i,5] = response$results[[1]]$geometry$location$lat
  data_file[i,6] = response$results[[1]]$geometry$location$lng
  Sys.sleep(0.3)
  print(paste(data_file[i,5], data_file[i,6], sep=", "))
}

write.csv(data_file, "data.csv")
