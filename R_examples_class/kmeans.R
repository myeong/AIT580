x <- rbind(matrix(rnorm(100, sd = 0.3), ncol = 2),
           matrix(rnorm(100, mean = 1, sd = 0.3), ncol = 2))
colnames(x) <- c("x", "y")

# Clustering (K=2, two-dimensional array)
cl <- kmeans(x, 2)
print(cl$cluster)
print(cl$centers)

# Clustering (K=3, two-dimensional array)
cl <- kmeans(x, 3)
print(cl$cluster)
print(cl$centers)
