# MusicGen Fine-Tuning Script

This Python script fine-tunes the **MusicGen** model using the **Replicate API**. The script is designed to start the fine-tuning process for a MusicGen model with a specific dataset and configuration. The resulting fine-tuned model will be saved to a destination under your account.

## Requirements

Before using this script, ensure you have installed the necessary dependencies:

```bash
pip install replicate
```

You also need an active account with Replicate and access to a valid dataset stored online, such as Firebase in this case.

## Script Overview

The script uses the `replicate` Python package to initiate the fine-tuning process for a MusicGen model. Fine-tuning adjusts the model to fit a specific style or dataset, making it more specialized.

### Key Features

- **Model Version**: The script fine-tunes a specific version of the MusicGen model: `sakemin/musicgen-fine-tuner:bc57274e2930af17c1d692516a4e6bd67618af425db3b2107c28c2100f031934`.
- **Dataset**: The model is fine-tuned on a dataset containing music samples that resemble the style of **Nick Mira**, provided via a Firebase URL.
- **Custom Configurations**: You can adjust hyperparameters like learning rate, number of epochs, and batch size to control how the model learns from the dataset.
  
### Training Parameters:

- **Dataset Path**: The dataset is stored online in Firebase Storage, which is accessed via a direct link.
- **Description**: The model is trained using the phrase `in the style of Nick Mira` to influence how it generates or interprets music data.
- **Drop Vocals**: Set to `True`, meaning that the fine-tuning process will exclude vocals.
- **Model Version**: The script fine-tunes the "melody" version of the model.
- **Learning Rate**: The learning rate is set to `1e-4` for model optimization.
- **Epochs**: The training will run for 3 epochs, which defines how many times the dataset will be passed through the model.
- **Batch Size**: The batch size is set to 16, controlling how many samples are processed at a time during training.

### Script Breakdown

1. **Fine-Tuning the Model**: The script initiates fine-tuning using the Replicate API. It passes the dataset link and fine-tuning parameters, including learning rate, epochs, and batch size.
   
2. **Training Status**: The script prints the current training status to the console, allowing you to monitor the fine-tuning process.

### Example Usage

1. Clone or download the script and ensure you have the required dependencies installed.
2. Update the `dataset_path` if you want to use a different dataset.
3. Run the script:

   ```bash
   python train_musicgen.py
   ```

4. Once the process begins, the script will print the training status, and the fine-tuned model will be stored in the destination specified as `twosyntaxerrors/musicgen-mira`.

## Output

- **Destination**: The fine-tuned model is saved to `twosyntaxerrors/musicgen-mira` on Replicate.

## Customization

You can modify the training parameters to suit your dataset and requirements:
- **Change the model version** if you want to fine-tune a different version of MusicGen.
- **Adjust the learning rate (`lr`)**, the number of epochs, and batch size to experiment with different training strategies.
- **Use a different dataset** by replacing the Firebase URL in the `dataset_path`.
