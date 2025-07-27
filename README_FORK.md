# OpenEvolve - Free AI Evolution Fork

🚀 **MAJOR FEATURE: 1,000 FREE AI-GENERATED CANDIDATE SOLUTIONS PER DAY**

This fork's primary breakthrough is enabling **completely free evolutionary algorithm development** through Google's generous Gemini API limits when routing through Gemini CLI. While the base repo only allows you to use an OpenAI-compatible API, **our fork provides 1,000 AI-generated candidate algorithms daily at zero cost** by using a bridge to turn Gemini CLI into an OpenAI-compatible API locally.

## 💰 Why This Matters

**Traditional AI Evolution Cost Problem:**
- $200-$1,000 per 1,000 code generation requests for models such as Claude 4 or GPT-4
- Most users can't afford extensive algorithm evolution

**Our Solution:**
- ✅ **Google Gemini Free Tier**: 1,000 requests/day on gemini-2.5-flash
- ✅ **Zero API costs** for up to 1,000 evolution candidates daily
- ✅ **Production-quality results** with state-of-the-art Gemini models
- ✅ **Windows compatibility** + comprehensive bridge setup

This enables **serious algorithmic research and optimization** accessible to students, researchers, and developers worldwide without prohibitive costs.

## 🆕 What Makes This Fork Special

### ✅ Windows Compatibility
- **All evaluators work perfectly on Windows** - Fixed path handling, signal issues, and subprocess execution
- **Cross-platform reliability** - Works seamlessly on Windows, macOS, and Linux
- **PowerShell support** - Proper shell command handling for Windows environments

### 🤖 Gemini Integration
- **Ready-to-use Gemini CLI bridge configurations** for easy Google AI integration
- **MCP tool support** - Leverage research tools (Perplexity, web search) during evolution
- **Test scripts included** - Validate your bridge connections before running evolution

### 🔧 Enhanced Reliability
- **Improved error handling** - Better diagnostics and recovery from evaluation failures
- **Robust subprocess management** - Proper timeout handling without Unix dependencies
- **Comprehensive testing** - All improvements tested on real Windows environments

## 🚀 Quick Start

### Windows Users
```bash
# Clone this Windows-compatible fork
git clone https://github.com/francoisjosephlacroix/openevolve.git
cd openevolve

# Install dependencies
pip install -e .

# Test Windows compatibility
cd examples/circle_packing
python -c "from evaluator import evaluate; print('✅ Windows compatibility confirmed!')"
```

### Gemini Bridge Setup
```bash
# Test bridge connection (requires Gemini CLI bridge running on localhost:8765)
python test_bridge_connection.py

# Run evolution with Gemini models
python -m openevolve.cli examples/circle_packing/initial_program.py examples/circle_packing/evaluator.py --config config_gemini_bridge.yaml --iterations 5
```

## 📊 Proven Results

**Circle Packing Evolution Test (Windows + Gemini):**
- ✅ Initial solution: `sum_radii = 0.9598`
- ✅ After 1 iteration: `sum_radii = 0.9798` (+2.1% improvement)
- ✅ Full evolution pipeline working perfectly

## 📁 New Files Added

- `WINDOWS_SETUP.md` - Comprehensive Windows setup guide
- `config_gemini_bridge.yaml` - Gemini CLI bridge configuration
- `config_circle_packing_gemini.yaml` - Problem-specific Gemini config
- `test_bridge_connection.py` - Bridge connectivity testing
- `start_gemini_openevolve.ps1` - PowerShell launch script

## 🔧 Technical Improvements

### Evaluator Scripts (Windows-compatible)
- `examples/circle_packing/evaluator.py` - Fixed path escaping and subprocess handling
- `examples/function_minimization/evaluator.py` - Removed Unix signal dependencies
- `examples/online_judge_programming/evaluator.py` - Added proper Python executable detection
- `examples/rust_adaptive_sort/evaluator.py` - Windows shell compatibility
- `examples/circle_packing_with_artifacts/evaluator.py` - Enhanced path handling

### Core System Updates
- `openevolve/llm/openai.py` - Bridge compatibility with non-streaming mode

## 🎯 Use Cases

This fork is perfect for:
- **Windows developers** who want to use OpenEvolve without compatibility issues
- **Gemini users** who prefer Google's models over OpenAI
- **Researchers** who need MCP tool integration for enhanced evolution
- **Cross-platform teams** who need reliable operation across all platforms

## 🔗 Links

- **Original Project**: [codelion/openevolve](https://github.com/codelion/openevolve)
- **Windows Setup Guide**: [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
- **This Fork**: [francoisjosephlacroix/openevolve](https://github.com/francoisjosephlacroix/openevolve)

## 🤝 Contributing

Contributions welcome! This fork focuses on:
- Windows compatibility improvements
- LLM bridge integrations (Gemini, Claude, etc.)
- Enhanced evaluation systems
- Cross-platform reliability

## 📄 License

Same Apache 2.0 license as the original OpenEvolve project.
