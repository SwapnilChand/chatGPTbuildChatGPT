def calculate_perplexity(model, dataset):
    loss = model.evaluate(dataset)
    perplexity = np.exp(loss)
    return perplexity
