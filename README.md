# Pollination Streamlit

A [Pollination](https://pollination.cloud) extension to facilitate working with
Pollination in [Streamlit](https://streamlit.io) apps.


Many thanks to the Streamlit team for developing [Streamlit app framework](https://github.com/streamlit/)! :balloon: :balloon: :balloon:

You can build custom apps for environmental building simulation by bringing the power of
Pollination and Ladybug Tools to Streamlit apps!

# Getting Started

See [this repository](https://github.com/pollination/sample-apps) for several sample
pollination sample apps.

If you are new Streamlit see Streamlit [get started documentation](https://docs.streamlit.io/library/get-started).

## Installation

`python -m pip install -U pollination-streamlit`

## Local Development
1. Clone this repo locally
```console
git clone git@github.com:ladybug-tools/pollination-streamlit

# or

git clone https://github.com/ladybug-tools/pollination-streamlit
```
2. Install dependencies:
```console
cd pollination-streamlit
pip install -r dev-requirements.txt
pip install -r requirements.txt
```

3. Run Tests:
```console
python -m pytest tests/
```
