set.seed(42)

n_episodes <- 1000
alpha <- 0.20
old_value <- 10

mc_data <- data.frame(
  Episode = integer(),
  Episode_Length = integer(),
  Total_Reward = numeric(),
  Discount_Factor = numeric(),
  Return_G = numeric(),
  Old_Value = numeric(),
  Updated_Value = numeric()
)

for(ep in 1:n_episodes){

  episode_length <- sample(8:25, 1)
  total_reward <- sample(10:40, 1)
  gamma <- round(runif(1, 0.90, 0.99), 2)
  return_g <- round(total_reward * gamma, 2)

  updated_value <- round(old_value + alpha * (return_g - old_value), 2)

  mc_data <- rbind(mc_data, data.frame(
    Episode = ep,
    Episode_Length = episode_length,
    Total_Reward = total_reward,
    Discount_Factor = gamma,
    Return_G = return_g,
    Old_Value = round(old_value,2),
    Updated_Value = updated_value
  ))

  old_value <- updated_value
}

head(mc_data)
tail(mc_data)
summary(mc_data)

write.csv(
  mc_data,
  "MonteCarlo_MC_1000_Dataset.csv",
  row.names = FALSE
)

cat("Dataset generated successfully!\n")
cat("Rows:", nrow(mc_data), "\n")
cat("Columns:", ncol(mc_data), "\n")

rm(list = ls())

library(ggplot2)

set.seed(123)

n <- 1000

Episode <- 1:n
Episode_Length <- sample(8:25, n, replace = TRUE)
Reward <- sample(10:40, n, replace = TRUE)
Gamma <- runif(n, 0.90, 0.99)
Return_G <- round(Reward * Gamma, 2)

alpha <- 0.20

Old_Value <- numeric(n)
Updated_Value <- numeric(n)

Old_Value[1] <- 10

for(i in 1:n){

  if(i > 1){
    Old_Value[i] <- Updated_Value[i-1]
  }

  Updated_Value[i] <- Old_Value[i] +
    alpha * (Return_G[i] - Old_Value[i])

}

mc_data <- data.frame(
  Episode,
  Episode_Length,
  Reward,
  Gamma,
  Return_G,
  Old_Value,
  Updated_Value
)

cat("\n=============================\n")
cat("First 10 Records\n")
cat("=============================\n")

head(mc_data,10)

cat("\n=============================\n")
cat("Summary Statistics\n")
cat("=============================\n")

summary(mc_data)

cat("\n=============================\n")
cat("Dataset Structure\n")
cat("=============================\n")

str(mc_data)

cat("\n=============================\n")
cat("Correlation Matrix\n")
cat("=============================\n")

cor(mc_data[,2:7])

ggplot(mc_data,
       aes(Episode_Length)) +
  geom_histogram(
    fill = "steelblue",
    color = "black",
    bins = 15
  ) +
  labs(
    title = "Episode Length Distribution",
    x = "Episode Length",
    y = "Frequency"
  )

ggplot(mc_data,
       aes(Reward)) +
  geom_histogram(
    fill = "forestgreen",
    color = "black",
    bins = 15
  ) +
  labs(title = "Reward Distribution")

ggplot(mc_data,
       aes(Return_G)) +
  geom_histogram(
    fill = "orange",
    color = "black",
    bins = 15
  ) +
  labs(title = "Monte Carlo Return Distribution")

ggplot(mc_data,
       aes(Episode,
           Updated_Value)) +
  geom_line(
    color = "red",
    linewidth = 1
  ) +
  labs(
    title = "Monte Carlo Learning Curve",
    x = "Episode",
    y = "Updated Value"
  )

ggplot(mc_data,
       aes(Episode,
           Reward)) +
  geom_line(color = "blue") +
  labs(title = "Reward per Episode")

ggplot(mc_data,
       aes(Episode,
           Return_G)) +
  geom_line(color = "purple") +
  labs(title = "Return per Episode")

ggplot(mc_data,
       aes(Updated_Value)) +
  geom_histogram(
    fill = "gold",
    color = "black",
    bins = 20
  ) +
  labs(title = "Updated Value Distribution")

par(mfrow = c(2,2))

boxplot(
  mc_data$Episode_Length,
  col = "skyblue",
  main = "Episode Length"
)

boxplot(
  mc_data$Reward,
  col = "lightgreen",
  main = "Reward"
)

boxplot(
  mc_data$Return_G,
  col = "orange",
  main = "Return"
)

boxplot(
  mc_data$Updated_Value,
  col = "pink",
  main = "Updated Value"
)

par(mfrow = c(1,1))

ggplot(mc_data,
       aes(Reward,
           Updated_Value)) +
  geom_point(
    color = "darkred",
    alpha = 0.6
  ) +
  geom_smooth(
    method = "lm",
    color = "black"
  ) +
  labs(title = "Reward vs Updated Value")

pairs(
  mc_data[,2:7],
  col = "blue",
  pch = 19
)

write.csv(
  mc_data,
  "MonteCarlo_1000_Dataset.csv",
  row.names = FALSE
)

cat("\n=====================================\n")
cat("Monte Carlo Simulation Completed\n")
cat("=====================================\n")

cat("Total Episodes :", nrow(mc_data), "\n")
cat("Total Variables:", ncol(mc_data), "\n")

cat("\nDataset saved as:\n")
cat("MonteCarlo_1000_Dataset.csv\n")
