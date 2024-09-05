# ICS CTF 2024 - Register the Dots - 1

**Title:** Register the Dots - 1

**Description:** During a regular audit of system startup behavior, a network connection was observed from Benji, an IT worker for Driftveil City.  
  
Benji ran the tool suite KAPE (Kroll Artifact Parser And Extractor) on her computer and would like your assistance analyzing the resulting KAPE capture data.  
  
What is the file name that caused this unexpected network traffic during startup?  
  
_Flag format: file name of executable. Example: **thing.exe**_  
  
Note: network traffic from Benji's computer is logged by Driftveil SOC and is therefore NOT located in Malcolm

## Solution:
I first extracted the zip file, my first step was going to `Startup` folders but couldn't find anything there, then I went to `C/Windows/System32/Tasks` and found a XML document named `FileZilla Auto Connect Server`, let's have a look at it:
```xml
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2024-06-18T17:30:51.8733038</Date>
    <Author>DESKTOP-P7JUKMH\Benji</Author>
    <Description>Filezilla auto connect to FTP server from configuration</Description>
    <URI>\FileZilla Auto Connect Server</URI>
  </RegistrationInfo>
  <Triggers />
  <Principals>
    <Principal id="Author">
      <RunLevel>LeastPrivilege</RunLevel>
      <UserId>DESKTOP-P7JUKMH\Benji</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>

    <ExecutionTimeLimit>P3D</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Users\Benji\AppData\Local\Temp\ditto.exe</Command>
    </Exec>
  </Actions>
</Task>
```

Hmm, we see a file named `ditto.exe`, and that's what we're searching for, and it's the flag for this challenge.
