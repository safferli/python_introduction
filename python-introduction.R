require(devtools)
library(httr)
set_config(use_proxy(url="10.26.0.16", port=3128))
install_github("ramnathv/slidify")
install_github("ramnathv/slidifyLibraries")

library(slidify)

wd <- "M:/Documents/games/gitlab/internal_presentations/python"
#wd <- "C:/Users/christoph.safferling/Documents/games/gitlab/internal_presentations/python"
setwd(wd)

## get number of PyPi packages
library(RCurl)
library(stringr)
# curl magic to get past Ubisoft proxy
options(RCurlOptions = list(proxy="10.26.0.16", proxyport=3128))
webpage <- getURL("https://pypi.python.org/pypi", ssl.verifypeer = FALSE)
# find package numbers; \\D is "not digit"
pypi <- gsub("\\D", "", str_extract(webpage, "<strong>[0-9]*</strong>"))
pypi_date <- Sys.Date()

author("python-introduction")
slidify("index.Rmd")
