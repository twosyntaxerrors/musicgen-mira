import replicate

# Start the fine-tuning process for the MusicGen model
training = replicate.trainings.create(
    version="sakemin/musicgen-fine-tuner:bc57274e2930af17c1d692516a4e6bd67618af425db3b2107c28c2100f031934",
    input={
        "dataset_path": "https://firebasestorage.googleapis.com/v0/b/loopgen-nextjs.appspot.com/o/sounds%2Fuser_2kwQgyxO8iGZt6owcA6WqG5uZ3U%2FNick%20Mira%20Training%20Data.zip?alt=media&token=8bfcd669-9998-483d-a65f-34ccd9719071",  # Firebase link
        "one_same_description": "in the style of Nick Mira",
        "drop_vocals": True,
        "model_version": "melody",
        "lr": 1e-4,
        "epochs": 3,
        "batch_size": 16
    },
    destination="twosyntaxerrors/musicgen-mira"
)

# Print the training status
print(training)
