def GetPredictions(model, comment):
    
    predictions = model.predict([comment])

    return predictions[0]