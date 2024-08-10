import re

pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
patternOK = r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}' # Patrón con barra en la fecha, sin milisegundos ni zona horaria (Ej: 2024/05/04 15:07:08)


text = """
//--------------------------------------------------------------------------------------------------
//-- Generated by: ???????
//-- Pass ID: 10020240630024045
//--        AOS = 2024/06/30 02:40:54;
//--        LOS = 2024/06/30 02:55:00;
//--        MAIN_PASS = false;
//-- Generation Based on: 
//-- 	 Prepass:	GenericPrePass(Version 1.0)
//-- 	 Pass:	NominalPassWithTimeShift(Version 1.0)
//-- 	 Postpass:	GenericPostPass(Version 1.0)
//-- 	 TT Command:	WithTCUplinkCtrlWithTimeShift(Version 1.0)
//-- 	 RT Command:	TemplateCommandRT(Version 1.0)
//-- 	 TT List Commands:	CommandsTT(Version 1.0)
//-- 	 RT List Commands:	CommandsRT(Version 1.0)
//-- 	 Unattended Pass:	UnattendedPass(Version 1.0)
//--------------------------------------------------------------------------------------------------
scl PrePass::GenericPrePass_10020240630024045
local 
    //--------------------------------------------------------------------------------------------------
	//Parameters Declaration
	string: passID;
	//--------------------------------------------------------------------------------------------------

	integer: FlagPrePassExecuted;
	string : prePassFlagName;
	string : station;
    boolean : continuePrePass;
    boolean : stationFromPassID;
{
	//--------------------------------------------------------------------------------------------------
		//Parameters Initialization
		passID = "10020240630024045";
		//--------------------------------------------------------------------------------------------------
	
    
    continuePrePass = true;
    stationFromPassID = true;
    station = "";

	//step = 100
    if (continuePrePass){
        prePassFlagName = AUX::PrePassExecutionFlagExistanceCheck(passID);
    }

	//step = 101
    if (continuePrePass){
        AUX::PrePassUnitsAliveness(passID);
    }

    //step = 102
    if (continuePrePass){
        AUX::PrePassRegisterScriptStartAndOperatorRecord;
    }

    //step = 103
    if (continuePrePass){
        AUX::PrePassOpenSessionUnits(passID);
    }
	
    //step = 104
    if (continuePrePass){                                                                      //Si no hace falta identificar cadena Revisar Script
        continuePrePass = AUX::PrePassChainConfiguration(stationFromPassID, passID, station);  //Si no hace falta identificar cadena Revisar Script
    }

    //step = 105
    if (continuePrePass){                                         //Revisar para que se usaba
        continuePrePass = AUX::PrePassEnableTelemetryVariables;   //Revisar para que se usaba
    }

	//step = 106                                  
    if (continuePrePass){                             
        AUX::PrePassSCCESetUpExpectedConfiguration;   
    }                                                 
    
    //step = 107
    AUX::PrePassRegisterScriptEnd(prePassFlagName, continuePrePass);
}

scl PostPass::GenericPostPass_10020240630024045
local
    //--------------------------------------------------------------------------------------------------
    //Parameters Declaration
    string: passID;
    //--------------------------------------------------------------------------------------------------

{
    //--------------------------------------------------------------------------------------------------
    //Parameters Initialization
    passID = "10020240630024045";
    //--------------------------------------------------------------------------------------------------


    //step = 100
    AUX::PostPassRegisterScriptStart;

    //step = 101
	AUX::PostPassCloseSessionPass;
	
    //step = 102
    AUX::PostPassRegisterScriptEnd(passID);
}

scl Pass::NominalPassWithTimeShift_10020240630024045

local
    //--------------------------------------------------------------------------------------------------
	//Parameters Declaration
	string: passID;
	time: AOS;
	time: LOS;
	boolean: MAIN_PASS;	//Agregado para saber si es pasada main o backup
	//--------------------------------------------------------------------------------------------------

    integer : dT_LOS, dT_BeforeAOS, dT_AfterAOS;
    integer : skipToStep;
    boolean : underContingency, continuePass;
    time : AOSWithTimeShift;
    time : LOSWithTimeShift;

    //Recovery Variables 
    string : InfFilesData;
    
{
       //--------------------------------------------------------------------------------------------------
       //Parameters Initialization
       passID = "10020240630024045";
       AOS = 2024/06/30 02:40:54;
       LOS = 2024/06/30 02:55:00;
       MAIN_PASS= false;
       //--------------------------------------------------------------------------------------------------

	continuePass = true;
	underContingency = false;
    AOSWithTimeShift = AOS + AUX::deltaTimeShift();
    LOSWithTimeShift = LOS + AUX::deltaTimeShift();
	
	//step = 1 - Load values in local variables
    AUX::LocalVarsSetting(#result dT_BeforeAOS, dT_AfterAOS, dT_LOS);

	//step = 2 - The pass and operator are registered in logs
    underContingency = AUX::RegisterPassScriptStartAndOperatorRecord(AOSWithTimeShift #result skipToStep);
    
	//step = 3 - Check if PrePass was executed
    if (AUX::EFC(3, skipToStep, underContingency)) {
        continuePass = AUX::PrePassExecutionCheck(passID);
    }

    //step = 4 - Check AOS time
	if (continuePass && AUX::EFC(4, skipToStep, underContingency)) {
        continuePass = AUX::AOSCheck(AOSWithTimeShift, dT_BeforeAOS, dT_AfterAOS);
    }
    
    //step = 8 Verifies the presence of  Recoveries or Reinforcements Action and validates its data.        //RRA definicion
    if (continuePass && AUX::EFC(8, skipToStep, underContingency)) {                                        //RRA definicion
        InfFilesData = SYS::RRALoadAndCheckInfFiles(passID, AOSWithTimeShift, LOSWithTimeShift);            //RRA definicion
    }

    //step = 9 Verifies the presence of Backup2MainPass file (mainpass_passID.inf) a contingency in the last pass        //Backup2MainPass check&update variable
    //if (continuePass && AUX::EFC(8, skipToStep, underContingency)) {                                                     //Backup2MainPass check&update variable
    //    MAIN_PASS = AUX::Backup2MainCheckAndLoadInfFile(passID, MAIN_PASS);           	                                 //Backup2MainPass check&update variable
    //}
    
    //step = 10 - Contact Management. Check Tlmy and command capabilities
    if (continuePass && AUX::EFC(10, skipToStep, underContingency)) {
        underContingency = underContingency || SYS::ContactManagement(passID, AOSWithTimeShift, LOSWithTimeShift);
    }
    
    //step = 11 - SOH - Contingency Actions
    if (continuePass && AUX::EFC(11, skipToStep, underContingency)) {
        underContingency = underContingency || SYS::ObservatorySOHCheck(passID, AOSWithTimeShift, LOSWithTimeShift);
    }

    //step = 20 - Time tagged commands upload ##Agregado MAIN_PASS- si "true" envia TT, si "false" saltea el step 20
    // funciona para planificacion nominal. Falta ver quien cambia a true una pasada backup que se necesita porque se perdió la main y a su vez q actualice el CommandsTT_PASS_ID con los comandos.
    // Poner condicion cuando chequea q el script tiene MAIN_PASS == false
    if (continuePass && AUX::EFC(20, skipToStep, underContingency) && MAIN_PASS) {
        TTListCommands::CommandsTT_10020240630024045;
    }
    
    //step = 30 - Real Time commands upload or Templates executions (RTOT)
    if (continuePass && AUX::EFC(30, skipToStep, underContingency)) {
    
    }
    
    //step = 31 Recovery and Reinforcement Action execution
    if (continuePass && AUX::EFC(31, skipToStep, underContingency)) {
        SYS::RRAExec(PassID, AOSWithTimeShift, LOSWithTimeShift, InfFilesData);

	//Definido en SAO ver q conviene    	    
	}
    
    //step = 32 - On Demand Activities - Ex: LMA - A definir funciones
//    if (continuePass && AUX::EFC(32, skipToStep, underContingency)) {
//       SYS::OnDemandActExec(PassID, AOSWithTimeShift, LOSWithTimeShift, InfFilesActivity); //Por definir
//    }    
    
    //step = 40 - SOH loop.
    if (continuePass && AUX::EFC(40, skipToStep, underContingency)) {
        underContingency = underContingency || SYS::WaitLOS_ObservatorySOHLoop(passID, AOSWithTimeShift, LOSWithTimeShift);
    }
    
    //step = 41 - Log register the end of pass script
    if (continuePass && AUX::EFC(41, skipToStep, underContingency)) {
        AUX::RegisterPassScriptEnd(passID, LOSWithTimeShift);
    }
}

scl UnattendedPass::UnattendedPass_10020240630024045

local
     //--------------------------------------------------------------------------------------------------
     //Parameters Declaration
     string: passID;
     time: AOS;
     time: LOS;
     //--------------------------------------------------------------------------------------------------
 
   string : aux;
{
     //--------------------------------------------------------------------------------------------------
     //Parameters Initialization
       passID = "10020240630024045";
       AOS = 2024/06/30 02:40:54;
       LOS = 2024/06/30 02:55:00;
     //--------------------------------------------------------------------------------------------------

	aux = AOS;
	LogGen("[UnattendedPass] AOS: " + aux);
	aux = LOS;
	LogGen("[UnattendedPass] LOS: " + aux);
  

	//Waiting 10 mins before AOS to execute Pre-Pass
        LogGen("[UnattendedPass] Waiting 10 mins before AOS to execute Pre-Pass");
     
	 while(CAS.Time < AOS - mins(10));
	 
	//100 Pre Pass Call
    PrePass::GenericPrePass_10020240630024045;

	//Waiting 3 mins before AOS to execute Pass
	
	LogGen("[UnattendedPass] Waiting 3 mins before AOS to execute Pass");
	
	while (CAS.Time  < AOS - mins(3));
	//200 Pass Call
    Pass::NominalPassWithTimeShift_10020240630024045;

    	//Waiting 2 mins after LOS to execute Pass
	LogGen("[UnattendedPass] Waiting 2 mins after LOS to execute Pass");
	
	while (CAS.Time > LOS + mins(2));

	//300 Post Pass Call
    PostPass::GenericPostPass_10020240630024045;
	
}


	scl RTListCommands::CommandsRT_10020240630024045

	local
		 //--------------------------------------------------------------------------------------------------
		 //Parameters Declaration
		 string: passID;
		 time: AOS;
		 time: LOS;
		 //--------------------------------------------------------------------------------------------------

	{
		 //--------------------------------------------------------------------------------------------------
		 //Parameters Initialization
		   passID = "10020240630024045";
		   AOS = 2024/06/30 02:40:54;
		   LOS = 2024/06/30 02:55:00;
		 //--------------------------------------------------------------------------------------------------
	 
		
	}


scl TTListCommands::CommandsTT_10020240630024045

local
    //--------------------------------------------------------------------------------------------------
	//Parameters Declaration
	string: passID;
	time: AOS;
	time: LOS;
	integer: SM;
	//--------------------------------------------------------------------------------------------------

{
     //--------------------------------------------------------------------------------------------------
     //Parameters Initialization
       passID = "10020240630024045";
       AOS = 2024/06/30 02:40:54;
       LOS = 2024/06/30 02:55:00;
	   SM = 515;
     //--------------------------------------------------------------------------------------------------
 

//	sme.ttcmd.begin.system( CAS.Time );
//	sme.ttcmd.begin.system.centralized.mode; 
 	 
	
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 36");
    sme.ttcmd.begin(4, 2024-07-01 01:40:57.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 37");
    sme.ttcmd.begin(0, 2024-07-01 01:41:57.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 38");
    sme.ttcmd.begin(12, 2024/07/01 01:47:21, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 39");
    sme.ttcmd.begin(18, 2024/07/01 01:48:21, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 40");
    sme.ttcmd.begin(2, 2024-07-01 01:52:39.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 41");
    sme.ttcmd.begin(3, 2024-07-01 01:52:39.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 42");
    sme.ttcmd.begin(5, 2024-07-01 01:52:39.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 43");
    sme.ttcmd.begin(6, 2024-07-01 01:52:39.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 44");
    sme.ttcmd.begin(7, 2024-07-01 01:52:39.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 45");
    sme.ttcmd.begin(1, 2024-07-01 01:52:39.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 46");
    sme.ttcmd.begin(8, 2024-07-01 01:52:51.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 47");
    sme.ttcmd.begin(9, 2024-07-01 01:52:51.300000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 48");
    sme.ttcmd.begin(15, 2024/07/01 01:59:33, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 49");
    sme.ttcmd.begin(14, 2024/07/01 01:59:33, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 50");
    sme.ttcmd.begin(19, 2024/07/01 01:59:33, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 51");
    sme.ttcmd.begin(11, 2024/07/01 01:59:33, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 52");
    sme.ttcmd.begin(10, 2024/07/01 01:59:33, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 53");
    sme.ttcmd.begin(13, 2024/07/01 01:59:33, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 54");
    sme.ttcmd.begin(16, 2024/07/01 01:59:45, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 55");
    sme.ttcmd.begin(17, 2024/07/01 01:59:45, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 56");
    sme.ttcmd.begin(22, 2024/07/01 03:18:19, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 57");
    sme.ttcmd.begin(28, 2024/07/01 03:19:19, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 58");
    sme.ttcmd.begin(32, 2024/07/01 03:24:30, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 59");
    sme.ttcmd.begin(38, 2024/07/01 03:25:30, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 60");
    sme.ttcmd.begin(20, 2024/07/01 03:32:31, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 61");
    sme.ttcmd.begin(21, 2024/07/01 03:32:31, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 62");
    sme.ttcmd.begin(23, 2024/07/01 03:32:31, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 63");
    sme.ttcmd.begin(24, 2024/07/01 03:32:31, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 64");
    sme.ttcmd.begin(25, 2024/07/01 03:32:31, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 65");
    sme.ttcmd.begin(29, 2024/07/01 03:32:31, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 66");
    sme.ttcmd.begin(27, 2024/07/01 03:32:43, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 67");
    sme.ttcmd.begin(26, 2024/07/01 03:32:43, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 68");
    sme.ttcmd.begin(31, 2024/07/01 03:38:06, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 69");
    sme.ttcmd.begin(33, 2024/07/01 03:38:06, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 70");
    sme.ttcmd.begin(34, 2024/07/01 03:38:06, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 71");
    sme.ttcmd.begin(35, 2024/07/01 03:38:06, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 72");
    sme.ttcmd.begin(30, 2024/07/01 03:38:06, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 73");
    sme.ttcmd.begin(39, 2024/07/01 03:38:06, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 74");
    sme.ttcmd.begin(36, 2024/07/01 03:38:18, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 75");
    sme.ttcmd.begin(37, 2024/07/01 03:38:18, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 76");
    sme.ttcmd.begin(42, 2024/07/01 04:56:26, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 77");
    sme.ttcmd.begin(48, 2024/07/01 04:57:26, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 78");
    sme.ttcmd.begin(41, 2024/07/01 05:09:08, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 79");
    sme.ttcmd.begin(40, 2024/07/01 05:09:08, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 80");
    sme.ttcmd.begin(43, 2024/07/01 05:09:08, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 81");
    sme.ttcmd.begin(44, 2024/07/01 05:09:08, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 82");
    sme.ttcmd.begin(45, 2024/07/01 05:09:08, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 83");
    sme.ttcmd.begin(49, 2024/07/01 05:09:08, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 84");
    sme.ttcmd.begin(46, 2024/07/01 05:09:20, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 85");
    sme.ttcmd.begin(47, 2024/07/01 05:09:20, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 86");
    sme.ttcmd.begin(52, 2024/07/01 11:19:32, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 87");
    sme.ttcmd.begin(58, 2024/07/01 11:20:32, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 88");
    sme.ttcmd.begin(55, 2024/07/01 11:29:08, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 89");
    sme.ttcmd.begin(54, 2024/07/01 11:29:08, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 90");
    sme.ttcmd.begin(50, 2024/07/01 11:29:08, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 91");
    sme.ttcmd.begin(51, 2024/07/01 11:29:08, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 92");
    sme.ttcmd.begin(53, 2024/07/01 11:29:08, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 93");
    sme.ttcmd.begin(59, 2024/07/01 11:29:08, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 94");
    sme.ttcmd.begin(56, 2024/07/01 11:29:20, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 95");
    sme.ttcmd.begin(57, 2024/07/01 11:29:20, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 96");
    sme.ttcmd.begin(64, 2024-07-01 12:49:35.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 97");
    sme.ttcmd.begin(60, 2024-07-01 12:50:35.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 98");
    sme.ttcmd.begin(72, 2024/07/01 12:54:04, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 99");
    sme.ttcmd.begin(78, 2024/07/01 12:55:04, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 35");
    sme.ttcmd.begin(62, 2024-07-01 13:00:17.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 36");
    sme.ttcmd.begin(61, 2024-07-01 13:00:17.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 37");
    sme.ttcmd.begin(63, 2024-07-01 13:00:17.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 38");
    sme.ttcmd.begin(67, 2024-07-01 13:00:17.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 39");
    sme.ttcmd.begin(66, 2024-07-01 13:00:17.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 40");
    sme.ttcmd.begin(65, 2024-07-01 13:00:17.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 41");
    sme.ttcmd.begin(69, 2024-07-01 13:00:29.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 42");
    sme.ttcmd.begin(68, 2024-07-01 13:00:29.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 43");
    sme.ttcmd.begin(79, 2024/07/01 13:07:34, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 44");
    sme.ttcmd.begin(74, 2024/07/01 13:07:34, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 45");
    sme.ttcmd.begin(75, 2024/07/01 13:07:34, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 46");
    sme.ttcmd.begin(71, 2024/07/01 13:07:34, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 47");
    sme.ttcmd.begin(70, 2024/07/01 13:07:34, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 48");
    sme.ttcmd.begin(73, 2024/07/01 13:07:34, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 49");
    sme.ttcmd.begin(76, 2024/07/01 13:07:46, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 50");
    sme.ttcmd.begin(77, 2024/07/01 13:07:46, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 51");
    sme.ttcmd.begin(82, 2024/07/01 14:25:08, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 52");
    sme.ttcmd.begin(88, 2024/07/01 14:26:08, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 53");
    sme.ttcmd.begin(94, 2024-07-01 14:31:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 54");
    sme.ttcmd.begin(90, 2024-07-01 14:32:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 55");
    sme.ttcmd.begin(89, 2024/07/01 14:39:14, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 56");
    sme.ttcmd.begin(81, 2024/07/01 14:39:14, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 57");
    sme.ttcmd.begin(85, 2024/07/01 14:39:14, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 58");
    sme.ttcmd.begin(80, 2024/07/01 14:39:14, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 59");
    sme.ttcmd.begin(84, 2024/07/01 14:39:14, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 60");
    sme.ttcmd.begin(83, 2024/07/01 14:39:14, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 61");
    sme.ttcmd.begin(86, 2024/07/01 14:39:26, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 62");
    sme.ttcmd.begin(87, 2024/07/01 14:39:26, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 63");
    sme.ttcmd.begin(93, 2024-07-01 14:45:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 64");
    sme.ttcmd.begin(95, 2024-07-01 14:45:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 65");
    sme.ttcmd.begin(96, 2024-07-01 14:45:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 66");
    sme.ttcmd.begin(97, 2024-07-01 14:45:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 67");
    sme.ttcmd.begin(91, 2024-07-01 14:45:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 68");
    sme.ttcmd.begin(92, 2024-07-01 14:45:27.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 69");
    sme.ttcmd.begin(98, 2024-07-01 14:45:39.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 70");
    sme.ttcmd.begin(99, 2024-07-01 14:45:39.600000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOn CmdID: 71");
    sme.ttcmd.begin(104, 2024-07-01 16:12:33.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StoreTMFromDRAM CmdID: 72");
    sme.ttcmd.begin(100, 2024-07-01 16:13:33.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StoreTMFromDRAM();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.MITTable_Report CmdID: 73");
    sme.ttcmd.begin(101, 2024-07-01 16:22:27.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.MITTable_Report();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqDisable CmdID: 74");
    sme.ttcmd.begin(107, 2024-07-01 16:22:27.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqDisable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.RTAcqEnable CmdID: 75");
    sme.ttcmd.begin(106, 2024-07-01 16:22:27.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.RTAcqEnable();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.NewSessionsToDownload CmdID: 76");
    sme.ttcmd.begin(105, 2024-07-01 16:22:27.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.NewSessionsToDownload();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOn CmdID: 77");
    sme.ttcmd.begin(102, 2024-07-01 16:22:27.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOn();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXSOff CmdID: 78");
    sme.ttcmd.begin(103, 2024-07-01 16:22:27.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXSOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.aSetTXXOff CmdID: 79");
    sme.ttcmd.begin(109, 2024-07-01 16:22:39.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.aSetTXXOff();
    sme.ttcmd.end();

    
        //TC.TT
LogGen("Send Time Tagged TC name SB.FS.1.SM.OBC.StopDumpSessions CmdID: 80");
    sme.ttcmd.begin(108, 2024-07-01 16:22:39.700000+00:00, SM);
        TC::SB.FS.1.SM.OBC.StopDumpSessions();
    sme.ttcmd.end();

    
 
//	sme.ttcmd.end.system.centralized.mode;
//	sme.ttcmd.end.system;
}
"""
res = re.findall(pattern, text)
print(res)