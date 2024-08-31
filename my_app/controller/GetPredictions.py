def GetPredictions(model, comment):
    
    predictions = model.predict([comment])

    result = {
        0: "Not Spam",
        1: "Spam"
    }
    return result[predictions[0]]