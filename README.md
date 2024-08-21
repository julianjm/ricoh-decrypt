# Ricoh Decrypt

## Description
Ricoh Decrypt is a tool designed to decrypt settings files exported from the Ricoh printer web interface. These files are encrypted with a passphrase, and this tool allows you to easily decrypt them.

## Features
- Decrypt Ricoh printer settings files
- Extract hidden settings, such as email configuration, from the exported file
- Useful for pentesters and security researchers

It has been tested on a Ricoh IM C300 printer.

## Installation
1. Clone the repository: `git clone https://github.com/julianjm/ricoh-decrypt.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Export the settings file from the Ricoh printer web interface.
2. Run the decryption tool: `python ricoh_decrypt.py passphrase input.csv output.csv`

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [GPL 3](LICENSE).

## Disclaimer
Please note that this tool should only be used for legal and ethical purposes. The authors are not responsible for any misuse or illegal activities conducted with this tool.
