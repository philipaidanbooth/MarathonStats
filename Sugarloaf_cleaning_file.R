library(dplyr)
library(lubridate)
library(ggplot2)

df <- read.csv("Activities (1).csv") 

df_clean <- df %>% 
  mutate(date = ymd_hms(Date)) %>% 
  filter(Activity.Type != "Indoor Rowing",
         Activity.Type != "Indoor Cycling",
         Activity.Type != "Other",
         date > as.Date("2023-11-30"), 
         Distance != 620) %>% 
  arrange(Avg.Pace)




write.csv(df_clean, file = "Garmin_clean2.csv", row.names = FALSE)

update.packages(ask = FALSE, checkBuilt = TRUE)


update.packages(ask = FALSE, checkBuilt = TRUE)



.libPaths()


