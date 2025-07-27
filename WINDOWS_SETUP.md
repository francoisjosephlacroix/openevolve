# Windows Compatibility & Gemini Bridge Setup

This fork includes significant improvements for Windows compatibility and integration with Google's Gemini models via the Gemini CLI bridge.

## 🆕 What's New in This Fork

### Windows Compatibility Fixes
- ✅ **All evaluation scripts now work on Windows**
- ✅ **Cross-platform path handling** using `os.path.normpath()` 
- ✅ **Subprocess-based timeouts** instead of Unix-only signal handling
- ✅ **Proper Python interpreter detection** using `sys.executable`
- ✅ **Windows shell compatibility** with `shell=True` where needed

### Gemini Integration
- ✅ **Gemini CLI bridge configuration files** for seamless integration
- ✅ **Enhanced OpenAI LLM client** with bridge compatibility
- ✅ **Test scripts** for validating bridge connections
- ✅ **Working circle packing example** with Gemini models

## 🚀 Quick Start on Windows

### Prerequisites
1. Python 3.8+ installed
2. [Gemini CLI MCP OpenAI Bridge](https://github.com/your-bridge-repo) running on `localhost:8765`

### Installation
```bash
# Clone this fork
git clone https://github.com/francoisjosephlacroix/openevolve.git
cd openevolve

# Install dependencies
pip install -e .
```

### Running with Gemini Bridge
```bash
# Test the bridge connection
python test_bridge_connection.py

# Run circle packing evolution with Gemini
python -m openevolve.cli examples/circle_packing/initial_program.py examples/circle_packing/evaluator.py --config config_gemini_bridge.yaml --iterations 5
```

## 📁 New Configuration Files

### `config_gemini_bridge.yaml`
General Gemini bridge configuration with MCP tool integration.

### `config_circle_packing_gemini.yaml` 
Specialized configuration for circle packing problems with detailed geometric guidance.

### `config_circle_packing_with_tools.yaml`
Enhanced configuration that explicitly instructs Gemini to use MCP tools for research.

## 🔧 Windows-Specific Improvements

### Evaluation Scripts Updated
All evaluators in `/examples/` have been updated for Windows compatibility:

- `circle_packing/evaluator.py` - Fixed path handling and subprocess execution
- `function_minimization/evaluator.py` - Removed signal dependency  
- `online_judge_programming/evaluator.py` - Added sys.executable usage
- `rust_adaptive_sort/evaluator.py` - Added shell=True for Windows
- `circle_packing_with_artifacts/evaluator.py` - Enhanced path escaping

### Core System Updates
- `openevolve/llm/openai.py` - Enhanced bridge compatibility with `stream=False`

## 🧪 Testing

### Test Bridge Connection
```bash
python test_bridge_connection.py
```

### Test Evaluators
```bash
cd examples/circle_packing
python -c "
from evaluator import evaluate
result = evaluate('initial_program.py')
print('Windows compatibility test passed!')
print('Metrics:', result)
"
```

## 📊 Performance Results

Tested successfully on Windows with Gemini models:
- **Initial program**: sum_radii = 0.9598, combined_score = 0.3642
- **After 1 iteration**: sum_radii = 0.9798, combined_score = 0.3718
- **Improvement**: +2.1% increase in circle packing efficiency

## 🔗 Original Project

This is a fork of [OpenEvolve](https://github.com/codelion/openevolve) by CodeLion with Windows compatibility and Gemini integration improvements.

## 🤝 Contributing

Feel free to submit issues and pull requests! This fork focuses on:
- Windows compatibility improvements
- LLM bridge integrations  
- Enhanced evaluation systems
- Cross-platform reliability

## 📄 License

Same as original OpenEvolve project.
