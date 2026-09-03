library(dplyr)
library(ggplot2) 

monkey_2052 <- read.csv(
  "phase1-rstudio-sklearn/data/monkey_2052.csv",
  header = FALSE,
  col.names = c("time_days", "conc_ug_ml")
)

monkey_2054 <- read.csv(
  "phase1-rstudio-sklearn/data/monkey_2054.csv",
  header = FALSE,
  col.names = c("time_days", "conc_ug_ml")
)

monkey_2058 <- read.csv(
  "phase1-rstudio-sklearn/data/monkey_2058.csv",
  header = FALSE,
  col.names = c("time_days", "conc_ug_ml")
)

monkey_2059 <- read.csv(
  "phase1-rstudio-sklearn/data/monkey_2059.csv",
  header = FALSE,
  col.names = c("time_days", "conc_ug_ml")
)

monkey_2061 <- read.csv(
  "phase1-rstudio-sklearn/data/monkey_2061.csv",
  header = FALSE,
  col.names = c("time_days", "conc_ug_ml")
)

monkey_2211 <- read.csv(
  "phase1-rstudio-sklearn/data/monkey_2211.csv",
  header = FALSE,
  col.names = c("time_days", "conc_ug_ml")
)

monkey_2052$monkey <- "2052"
monkey_2054$monkey <- "2054"
monkey_2058$monkey <- "2058"
monkey_2059$monkey <- "2059"
monkey_2061$monkey <- "2061"
monkey_2211$monkey <- "2211"

six_monkeys <- bind_rows(monkey_2052, monkey_2054, monkey_2058,
                         monkey_2059, monkey_2061, monkey_2211)

ggplot(six_monkeys,aes(x=time_days, y=conc_ug_ml, colour = monkey)) + geom_point() 

ggsave("phase1-rstudio-sklearn/plot_all_monkeys_colour.png", width = 7, height = 5)

monkey_summary <- six_monkeys %>%
  group_by(monkey) %>%
  summarise(
    n_points  = n(),
    first_day = min(time_days),
    last_day  = max(time_days),
    span_days = max(time_days) - min(time_days)
  )

ggplot(monkey_2061,aes(x=time_days, y=conc_ug_ml, colour = monkey)) + geom_point() + geom_line()

ggsave("phase1-rstudio-sklearn/plot_monkey_2061_line.png", width = 7, height = 5)
