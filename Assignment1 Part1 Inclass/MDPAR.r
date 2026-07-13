library(igraph)
library(ggraph)
library(ggplot2)

edges <- data.frame(
  from = c(
    "MDP",
    "State",
    "Actions",
    "Transition",
    "Reward",
    "Policy",
    "Value",
    "Bellman",
    "Optimal Policy",
    "Execute"
  ),
  to = c(
    "State",
    "Actions",
    "Transition",
    "Reward",
    "Policy",
    "Value",
    "Bellman",
    "Optimal Policy",
    "Execute",
    "New State"
  )
)

graph <- graph_from_data_frame(edges)

ggraph(graph, layout = "tree") +
  geom_edge_link(
    arrow = arrow(length = unit(4, "mm"), type = "closed"),
    end_cap = circle(3, "mm"),
    colour = "gray40",
    width = 1.3
  ) +
  geom_node_label(
    aes(label = name),
    fill = c(
      "#1565C0","#BBDEFB","#C8E6C9","#FFE082",
      "#FFCCBC","#F8BBD0","#B2EBF2",
      "#DCEDC8","#FFF59D","#90CAF9","#A5D6A7"
    ),
    fontface = "bold",
    size = 4
  ) +
  theme_void() +
  ggtitle("MARKOV DECISION PROCESS")