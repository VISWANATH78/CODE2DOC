# AI Code Documentation Generator

## 🌟 Overview

The AI Code Documentation Generator is an innovative Python application leveraging the Groq API to automate comprehensive software documentation generation. By analyzing entire project codebases uploaded as zip files, this tool transforms raw code into structured, readable documentation.

## ✨ Features

- 📂 Full project zip file upload support
- 🤖 Automated code documentation generation
- 📄 Markdown documentation creation
- 🔄 Intelligent API rate limit handling with exponential backoff
- 📥 One-click documentation download
- 🔍 Deep code analysis using advanced AI models

## 🛠 Prerequisites

### System Requirements
- Python 3.x
- Stable internet connection
- Groq API Key

### Required Libraries
- `groq`: Groq API client
- `streamlit`: Web application framework
- Standard Python Libraries:
  - `os`
  - `zipfile`
  - `shutil`
  - `tempfile`
  - `time`
  - `logging`

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/ai-code-documentation-generator.git
cd ai-code-documentation-generator
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install groq streamlit
```

### 4. Configure API Key
- Open the script
- Replace `"API_KEY"` with your actual Groq API key

## 💻 Usage

### Launch Application
```bash
streamlit run app.py
```

### Documentation Generation Steps
1. Upload project zip file
2. Click "Analyze"
3. Review generated documentation
4. Download markdown file

## 🔬 Key Functions

### `analyze_code_with_groq()`
- Analyzes individual code files
- Uses Groq API with Llama 3.1 70B Versatile Model
- Implements intelligent code review

### `process_uploaded_zip()`
- Handles zip file extraction
- Creates temporary working directory
- Manages file processing safely

### `analyze_project_folder()`
- Recursively scans project structure
- Generates documentation for each file
- Supports nested project architectures

### `format_documentation()`
- Structures raw analysis into markdown
- Creates consistent documentation format
- Adds contextual sections like Description, Overview, Dependencies

## 🛡 Error Handling

### Robust Mechanisms
- Exponential backoff for API rate limits
- Comprehensive error logging
- Graceful error messages
- Retry logic for transient failures

## 📋 Documentation Structure

```markdown
# Documentation for <file_path>

## Description
Concise file purpose explanation

## Code Overview
Detailed functionality breakdown

## Key Functions/Classes
- Function/Class details
- Purpose and usage

## Dependencies
External libraries and modules

## Usage Examples
Practical code implementation guidance

## Additional Notes
Limitations, edge cases, recommendations
```

## 🌐 Technologies Ecosystem

- **Languages**: Python
- **Frameworks**: 
  - Streamlit
  - Groq API
- **AI Model**: Llama 3.1 70B Versatile
- **Documentation**: Markdown

## ⚙️ Customization Options

Easily modify in the script:
- Groq API key configuration
- Logging verbosity
- Model parameters
- Retry attempt configurations
- Error handling strategies

## ⚠️ Limitations & Considerations

- Dependent on Groq API availability
- Rate-limited API interactions
- Requires well-structured zip file input
- Documentation quality varies with code complexity
- Potential language/framework-specific nuances

## 🤝 Contributing

### Contribution Guidelines
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Reporting Issues
- Use GitHub Issues
- Provide detailed problem description
- Include reproducibility steps
- Share relevant error logs

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🌈 Future Roadmap

- [ ] Support more programming languages
- [ ] Enhanced AI analysis capabilities
- [ ] Improved error diagnostic features
- [ ] Integration with more code hosting platforms
- [ ] Customizable documentation templates

## 📞 Contact & Support

- Project Maintainer: viswanath v s
- Email: vichu110602@gmail.com

---

**Built with ❤️ by AI Documentation Team**
