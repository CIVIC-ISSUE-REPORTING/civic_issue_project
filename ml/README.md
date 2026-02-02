# Machine Learning Models

Training notebooks and models for the civic issue management system.

## Models

1. **Issue Classifier** - Classifies issues into categories (road, water, electricity, etc.)
2. **Severity Detector** - Determines issue severity (low, medium, high, critical)
3. **Spam Detector** - Identifies spam/fake issue reports
4. **Completion Verifier** - Verifies issue resolution using before/after images
5. **Priority Predictor** - Predicts issue priority based on multiple factors

## Datasets

- `raw/` - Original unprocessed data
- `processed/` - Cleaned and preprocessed data
- `synthetic/` - Synthetic data generated for training

## Notebooks

Each notebook contains:
- Data exploration
- Model training
- Evaluation metrics
- Model export

## Setup

```bash
pip install tensorflow keras scikit-learn pandas numpy matplotlib seaborn
```

## Training

```bash
jupyter notebook
# Open and run notebooks in the notebooks/ directory
```
