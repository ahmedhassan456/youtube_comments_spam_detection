def GetPredictions(model, author, vid_title, comment):
    
    predictions = model.predict([author + "  " + vid_title + "  " + comment])

    result = {
        0: "Not Spam",
        1: "Spam"
    }
    return result[predictions[0]]