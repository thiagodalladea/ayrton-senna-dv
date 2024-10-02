install.packages("ggplot2")
install.packages("reshape2")

# Carregar bibliotecas necessárias
library(ggplot2)
library(reshape2)

# Carregar os dados do arquivo CSV
data <- read.csv('data-csv/qualifying-results_ayrton-senna.csv')

# Criar uma tabela pivotada (como no Python) para formatar os dados
heatmap_data <- dcast(data, race ~ year, value.var = "position")

# Derreter os dados para um formato longo, que é aceito pelo ggplot2
long_data <- melt(heatmap_data, id.vars = "race", variable.name = "year", value.name = "position")

# Criar o heatmap
ggplot(long_data, aes(x = year, y = race, fill = position)) +
  geom_tile(color = "white") +
  scale_fill_gradient(low = "white", high = "red", na.value = "white") +
  labs(title = "Heatmap of Ayrton Senna Qualifying Results", x = "Year", y = "Race") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
