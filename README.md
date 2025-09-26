# RSS Sniper 🎯

A powerful Python tool for monitoring RSS feeds and filtering cybersecurity news based on customizable keywords. RSS Sniper helps security professionals, researchers, and organizations stay informed about relevant threats, vulnerabilities, and security news by automatically filtering through hundreds of RSS feeds from trusted sources.

## 🚀 Features

- **Multi-Source RSS Monitoring**: Monitors 100+ RSS feeds from journalists, vendors, government agencies, and security communities
- **Keyword-Based Filtering**: Customizable keyword categories for targeted content discovery
- **Categorized Output**: Organizes results by threat actors, vendors, and products
- **Cross-Platform Support**: Works on Windows, Linux, and macOS
- **Extensible Architecture**: Easy to add new RSS feeds and keyword categories

## 📋 Current Capabilities

### ✅ Implemented
- **News Monitoring**: Filter news articles based on customizable keywords
- **RSS Feed Parsing**: Parse and process RSS feeds from multiple sources
- **Keyword Matching**: Case-insensitive keyword matching in article titles
- **Output Generation**: Generate formatted reports saved to `news.txt`

### 🚧 In Development
- **Vendor Monitoring**: Track vendor-specific security updates and advisories
- **Product Monitoring**: Monitor specific product vulnerabilities and updates
- **CVE Tracking**: Track Common Vulnerabilities and Exposures (CVE) announcements

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
```bash
git clone <your-repo-url>
cd RSS-Sniper
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## 🔧 SSL Certificate Issues

Some RSS feeds may have SSL certificate issues (expired certificates, self-signed certificates, or HTTP connections). The feedparser library by default doesn't allow connections to unverified SSL certificates.

### Monkey-Patching Solution

To resolve SSL certificate issues, you need to monkey-patch the feedparser library. Add the following code to the `api.py` file in your feedparser installation:

```python
import ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
```

**Location of the file:**
- Windows: `venv\Lib\site-packages\feedparser\api.py`
- Linux/macOS: `venv/lib/python3.x/site-packages/feedparser/api.py`

**⚠️ Security Warning**: This bypasses SSL certificate verification. Only use this in trusted environments and consider the security implications.

### Alternative: Environment Variable

You can also set an environment variable to disable SSL verification:

```bash
# Windows
set PYTHONHTTPSVERIFY=0

# Linux/macOS
export PYTHONHTTPSVERIFY=0
```

## 📖 Usage

### Basic Usage

Monitor news articles based on your configured keywords:
```bash
python sniper.py -n
```

### Command Line Options

- `-n, --news`: Monitor news articles (currently implemented)
- `-v, --vendors`: Monitor vendor feeds (in development)
- `-p, --products`: Monitor product-specific feeds (in development)
- `-c, --cves`: Monitor CVE feeds (in development)

### Example Output

After running `python sniper.py -n`, the tool will:
1. Parse RSS feeds from configured sources
2. Filter articles based on your keyword categories
3. Generate a formatted report in `news.txt`

The output includes:
- Article title and publication date
- Source RSS feed name
- Article link
- Article summary
- Organized by keyword categories

## ⚙️ Configuration

### RSS Feeds (`config/rss_feeds.json`)

The tool monitors feeds from four main categories:

- **Journalists**: Security journalists and news outlets (BleepingComputer, Krebs on Security, etc.)
- **Vendors**: Security vendor blogs and advisories (Cisco, Microsoft, etc.)
- **Governments**: Government security agencies (US-CERT, BSI, etc.)
- **Communities**: Security communities and forums (Reddit, etc.)

### Keywords (`config/keywords.json`)

Configure keyword categories to filter relevant content:

- **Threat Actors**: APT groups, ransomware gangs, etc.
- **Vendors**: Technology vendors and products
- **Products**: Specific software and hardware products

### Vendors (`config/vendors.json`)

Configure vendor-specific monitoring (for future vendor tracking features).

## 📁 Project Structure

```
RSS-Sniper/
├── sniper.py              # Main application entry point
├── scope.py               # Core RSS parsing and filtering logic
├── scope_utils.py         # Utility functions for RSS processing
├── config/
│   ├── rss_feeds.json     # RSS feed configurations
│   ├── keywords.json      # Keyword categories and terms
│   └── vendors.json       # Vendor configurations
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Customization

### Adding New RSS Feeds

Edit `config/rss_feeds.json` to add new RSS feeds:

```json
{
    "Journalists": {
        "Your New Source": "https://example.com/feed.xml"
    }
}
```

### Adding New Keywords

Edit `config/keywords.json` to add new keyword categories:

```json
{
    "Your Category": [
        "keyword1",
        "keyword2",
        "keyword3"
    ]
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
2. **RSS Feed Errors**: Some feeds may be temporarily unavailable or have changed URLs
3. **Permission Errors**: Ensure the tool has write permissions for the output directory
4. **SSL Certificate Errors**: Use the monkey-patching solution above for feeds with certificate issues

### Debug Mode

For detailed error information, check the console output when running the tool.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional RSS feed sources
- Enhanced keyword matching algorithms
- Output format options (JSON, CSV, etc.)
- Real-time monitoring capabilities
- Web interface for configuration

## 📄 License

This is a Free Open Source Software, use it at your discretion

## 🙏 Acknowledgments

- RSS feed sources from https://github.com/thehappydinoa/awesome-threat-intel-rss
- Python feedparser library for RSS parsing 
- Security researchers and journalists who provide valuable content

## 📞 Support

For issues, questions, or contributions, please [create an issue](https://github.com/nullvaluefound/RSS-Sniper/issues) or [contact the maintainer](https://www.linkedin.com/in/john-mock-323a16165/).

---

**Note**: This tool is designed for legitimate security research and monitoring purposes. Please respect the terms of service of RSS feed providers and use responsibly.