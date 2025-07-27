#!/usr/bin/env python3
"""
Test script to verify OpenEvolve can connect to the Gemini CLI MCP OpenAI Bridge
"""

import os
import requests
import json
import asyncio
from openai import OpenAI

def test_bridge_connection():
    """Test basic connection to the bridge server"""
    bridge_url = "http://localhost:8765"
    
    print("🔍 Testing Gemini CLI Bridge Connection...")
    
    try:
        # Test 1: Check if bridge server is running
        print("\n1. Testing bridge server health...")
        response = requests.get(f"{bridge_url}/v1/models", timeout=10)
        if response.status_code == 200:
            models = response.json()
            print(f"✅ Bridge server is running!")
            print(f"   Available models: {len(models.get('data', []))} models")
            for model in models.get('data', [])[:3]:  # Show first 3 models
                print(f"   - {model.get('id', 'unknown')}")
        else:
            print(f"❌ Bridge server returned status {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to bridge server at http://localhost:8765")
        print("   Make sure to start the bridge server first:")
        print("   cd ../gemini-cli-mcp-openai-bridge")
        print("   node .\\gemini-cli\\packages\\bridge-server\\dist\\index.js --mode read-only --port 8765")
        return False
    except Exception as e:
        print(f"❌ Error connecting to bridge: {e}")
        return False
    
    # Test 2: Test chat completion
    print("\n2. Testing OpenAI-compatible API...")
    try:
        client = OpenAI(
            api_key="dummy-key",  # Bridge uses gemini-cli auth
            base_url="http://localhost:8765/v1"
        )
        
        response = client.chat.completions.create(
            model="gemini-2.0-flash-lite",
            messages=[
                {"role": "user", "content": "Hello! Can you write a simple Python function that adds two numbers?"}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        print("✅ Chat completion successful!")
        print(f"   Model: {response.model}")
        content = response.choices[0].message.content
        if len(content) > 100:
            print(f"   Response: {content[:100]}...")
        else:
            print(f"   Response: {content}")
        return True
        
    except Exception as e:
        print(f"❌ Chat completion failed: {e}")
        return False

def test_openevolve_config():
    """Test if OpenEvolve can load our custom configuration"""
    print("\n3. Testing OpenEvolve configuration...")
    
    try:
        import yaml
        
        # Load our custom config
        config_path = "config_gemini_bridge.yaml"
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        print("✅ Configuration file loaded successfully!")
        print(f"   API Base: {config['llm']['api_base']}")
        print(f"   Models: {[m['name'] for m in config['llm']['models']]}")
        print(f"   Max Iterations: {config['max_iterations']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration loading failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 OpenEvolve + Gemini CLI Bridge Integration Test")
    print("="*50)
    
    # Check if OpenEvolve is installed
    try:
        import openevolve
        print("✅ OpenEvolve is installed")
    except ImportError:
        print("❌ OpenEvolve is not installed. Run: pip install -e .")
        return
    
    # Run tests
    tests_passed = 0
    total_tests = 3
    
    if test_bridge_connection():
        tests_passed += 1
    
    if test_openevolve_config():
        tests_passed += 1
    
    # Test 3: Quick integration test
    print("\n4. Testing basic OpenEvolve initialization...")
    try:
        # Set dummy API key for testing
        os.environ["OPENAI_API_KEY"] = "dummy-key"
        
        from openevolve import OpenEvolve
        
        # Try to initialize (this will test config loading)
        evolve = OpenEvolve(
            initial_program_path="examples/function_minimization/initial_program.py",
            evaluation_file="examples/function_minimization/evaluator.py",
            config_path="config_gemini_bridge.yaml"
        )
        
        print("✅ OpenEvolve initialization successful!")
        tests_passed += 1
        
    except Exception as e:
        print(f"❌ OpenEvolve initialization failed: {e}")
    
    # Summary
    print(f"\n{'='*50}")
    print(f"🎯 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! OpenEvolve is ready to use with Gemini CLI Bridge.")
        print("\n🚀 Next steps:")
        print("   1. Start the bridge server (if not already running)")
        print("   2. Run an example with our custom config:")
        print("      python openevolve-run.py examples/function_minimization/initial_program.py \\")
        print("             examples/function_minimization/evaluator.py \\")
        print("             --config config_gemini_bridge.yaml --iterations 10")
    else:
        print("⚠️  Some tests failed. Please check the setup.")

if __name__ == "__main__":
    main()
