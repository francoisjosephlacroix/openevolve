# PowerShell script to start Gemini CLI Bridge and test OpenEvolve integration
param(
    [switch]$StartBridge = $false,
    [switch]$TestOnly = $false,
    [int]$Port = 8765,
    [string]$Mode = "read-only"
)

Write-Host "🚀 Gemini CLI Bridge + OpenEvolve Integration Launcher" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Green

# Paths
$bridgePath = "C:\Users\fjlac\CodingProjects\gemini-cli-mcp-openai-bridge"
$openevolvePath = "C:\Users\fjlac\CodingProjects\openevolve"
$bridgeBinary = "$bridgePath\gemini-cli\packages\bridge-server\dist\index.js"

# Function to check if bridge server is running
function Test-BridgeServer {
    param($port)
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:$port/v1/models" -TimeoutSec 5
        return $true
    }
    catch {
        return $false
    }
}

# Function to start bridge server
function Start-BridgeServer {
    param($port, $mode)
    
    Write-Host "`n🔧 Starting Gemini CLI Bridge Server..." -ForegroundColor Yellow
    Write-Host "   Port: $port" -ForegroundColor Cyan
    Write-Host "   Mode: $mode" -ForegroundColor Cyan
    Write-Host "   Path: $bridgeBinary" -ForegroundColor Cyan
    
    if (-not (Test-Path $bridgeBinary)) {
        Write-Host "❌ Bridge binary not found at: $bridgeBinary" -ForegroundColor Red
        Write-Host "   Please make sure the gemini-cli-mcp-openai-bridge project is built." -ForegroundColor Red
        return $false
    }
    
    # Start bridge server in background
    $job = Start-Job -ScriptBlock {
        param($binary, $port, $mode)
        Set-Location (Split-Path $binary)
        node $binary --mode $mode --port $port --debug
    } -ArgumentList $bridgeBinary, $port, $mode
    
    Write-Host "   Bridge server job started (ID: $($job.Id))" -ForegroundColor Green
    
    # Wait for server to start
    Write-Host "   Waiting for server to start..." -ForegroundColor Yellow
    $maxWait = 30
    $waited = 0
    
    while ($waited -lt $maxWait) {
        if (Test-BridgeServer -port $port) {
            Write-Host "✅ Bridge server is running on port $port!" -ForegroundColor Green
            return $job
        }
        Start-Sleep -Seconds 2
        $waited += 2
        Write-Host "." -NoNewline -ForegroundColor Gray
    }
    
    Write-Host "`n❌ Bridge server failed to start within $maxWait seconds" -ForegroundColor Red
    Stop-Job $job -ErrorAction SilentlyContinue
    Remove-Job $job -ErrorAction SilentlyContinue
    return $false
}

# Main execution
try {
    # Check if we're in the right directory
    if (-not (Test-Path "config_gemini_bridge.yaml")) {
        Write-Host "❌ Not in OpenEvolve directory or config file missing" -ForegroundColor Red
        Write-Host "   Current directory: $(Get-Location)" -ForegroundColor Red
        Write-Host "   Expected: $openevolvePath" -ForegroundColor Red
        exit 1
    }
    
    $bridgeJob = $null
    
    if ($StartBridge -or -not (Test-BridgeServer -port $Port)) {
        if (Test-BridgeServer -port $Port) {
            Write-Host "ℹ️  Bridge server already running on port $Port" -ForegroundColor Blue
        } else {
            $bridgeJob = Start-BridgeServer -port $Port -mode $Mode
            if (-not $bridgeJob) {
                Write-Host "❌ Failed to start bridge server" -ForegroundColor Red
                exit 1
            }
        }
    } else {
        Write-Host "✅ Bridge server already running on port $Port" -ForegroundColor Green
    }
    
    if (-not $TestOnly) {
        # Run the connection test
        Write-Host "`n🧪 Running integration tests..." -ForegroundColor Yellow
        
        $env:OPENAI_API_KEY = "dummy-key"  # Set dummy key for testing
        
        python test_bridge_connection.py
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n🎉 Integration test completed successfully!" -ForegroundColor Green
            Write-Host "`n🚀 Ready to run OpenEvolve examples:" -ForegroundColor Cyan
            Write-Host "   python openevolve-run.py examples/function_minimization/initial_program.py examples/function_minimization/evaluator.py --config config_gemini_bridge.yaml --iterations 10" -ForegroundColor White
        } else {
            Write-Host "`n⚠️  Integration test had some issues" -ForegroundColor Yellow
        }
    }
    
    # Keep bridge running if we started it
    if ($bridgeJob) {
        Write-Host "`n🔄 Bridge server is running in background (Job ID: $($bridgeJob.Id))" -ForegroundColor Blue
        Write-Host "   To stop: Stop-Job $($bridgeJob.Id); Remove-Job $($bridgeJob.Id)" -ForegroundColor Blue
        Write-Host "   To check status: Get-Job $($bridgeJob.Id)" -ForegroundColor Blue
        
        # Wait for user input to keep script alive
        Write-Host "`nPress Enter to stop the bridge server and exit..." -ForegroundColor Yellow
        Read-Host
        
        Write-Host "🛑 Stopping bridge server..." -ForegroundColor Yellow
        Stop-Job $bridgeJob -ErrorAction SilentlyContinue
        Remove-Job $bridgeJob -ErrorAction SilentlyContinue
        Write-Host "✅ Bridge server stopped" -ForegroundColor Green
    }
    
} catch {
    Write-Host "❌ Error: $_" -ForegroundColor Red
    if ($bridgeJob) {
        Stop-Job $bridgeJob -ErrorAction SilentlyContinue
        Remove-Job $bridgeJob -ErrorAction SilentlyContinue
    }
    exit 1
}

Write-Host "`n👋 Setup completed!" -ForegroundColor Green
