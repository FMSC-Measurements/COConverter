'''
Created on Jun 30, 2011

@author: benjaminjcampbell



'''
import collections
import Logger

log = Logger.Logger()



createdBy = 'COConver Utility'

import clr
clr.AddReference('CruiseDAL')
clr.AddReference('System')
from System import Array
from System import Object
from CruiseDAL import DAL

def toFloat(val):
    return float(val) if val else 0.0

#utility method for getting float values from metakit
#used for catching obviously corrupt values
#e(epsilon) is the smallest a value can be, before it is considered 0
#max is the largest value we can reasonably expect
def getattrFloat(source, attr, e=2.3283064e-10, max=2000000):
    value = None
    try:
        value = getattr(source, attr)
        if not isinstance(value, float):
            value = float(value)
    except:
        log.lg('low', "overriding value {0} on property {1} with 0.0 (float)".format(repr(value), attr))
        value = 0.0

    if value != 0.0 and (abs(value) < e or abs(value) > max):
        log.lg("high", "overriding value {0} on property {1} with 0.0 (float)".format(repr(value), attr))
        value = 0.0
    return value

def getattrInt(source, attr):
    value = 0
    try:
        value = getattr(source, attr)
        if not isinstance(value, int):
            value = int(value)
            pass
    except:
        log.lg("low", "overriding value {0} on property {1} with 0 (int)".format(repr(value), attr))
        value = 0
        pass
    return value


def readCruiseTable(vw, dal):
    from CruiseDAL.DataObjects import SaleDO
    log.lg('norm', 'START reading cruise table')
    for row in vw:
        sale = SaleDO(dal)
        sale.SaleNumber = getattr(row, 'SaleNo')
        sale.Name = row.SaleName
        sale.Purpose = row.Purpose
        sale.Region = row.Region
        sale.Forest = row.Forest
        sale.District = row.District
        sale.CalendarYear = getattrInt(row, 'CalYear')
        sale.Remarks = row.Remarks
        sale.Save()
        log.lg('low', 'Created Record :' + str(sale.rowID))

def readCuttingUnitsTable(vw, dal):
    from CruiseDAL.DataObjects import CuttingUnitDO
    log.lg('norm', 'START reading cuttingunits table')


    for row in vw:
        unit = CuttingUnitDO(dal)
        unit.Code = str.strip(row.CutUnit)
        unit.Area = getattrFloat(row, "Area")
        unit.Description = row.Description
        unit.LoggingMethod = row.LogMeth
        unit.PaymentUnit = row.PayUnit
        unit.Save()
        log.lg('low', 'Created Record :' + str(unit.rowID))

#         
        
def readStratumTable(vw, dal):

    log.lg('norm', 'START reading stratum table')
    from CruiseDAL.DataObjects import StratumDO
    from CruiseDAL.DataObjects import CuttingUnitDO


    for row in vw:
        stratum = StratumDO(dal)
        stratum.Code = str.strip(row.Stratum)
        stratum.Description = row.Description
        stratum.Method = row.CruzMeth if (row.CruzMeth != "PCMTRE") else "PCM"
        stratum.BasalAreaFactor = getattrFloat(row, "BAF")
        stratum.FixedPlotSize = getattrFloat(row, "FPSize")
        stratum.Month = row.Month
        stratum.Year = row.Year
        
        stratum.Save()
        log.lg('low', 'Created Record :' + str(stratum.rowID))
        unitCodes = row.Units.split(',')
        for c in unitCodes:
            prams = Array.CreateInstance(Object, 1)
            prams[0] = str.strip(c)
            unit = dal.ReadSingleRow[CuttingUnitDO]('CuttingUnit', 'WHERE Code = ?', prams)
            if not unit:
                log.lg('high', 'unable to locate Cutting Unit record in Stratum table. Unit Code: ' + c)
            stratum.CuttingUnits.Add(unit)
        stratum.CuttingUnits.Save()
    
def readSubPopTable(vw, dal):
    log.lg('norm','START reading subpopulation table')
    
    from CruiseDAL.DataObjects import StratumDO
    from CruiseDAL.DataObjects import SampleGroupDO
    from CruiseDAL.DataObjects import TreeDefaultValueDO

    for row in vw:
        prams = Array[Object]((str.strip(row.Stratum), ))

        currentSt = dal.ReadSingleRow[StratumDO]('Stratum', 'WHERE Code = ?', prams)
        if not currentSt:
            log.lg('high', 'unable to locate record for stratum in SubPopulation table:' + row.Stratum)
            
        currentSG = dal.ReadSingleRow[SampleGroupDO]('SampleGroup', 'WHERE Code = ? AND Stratum_CN = ?', Array[Object]((str.strip(row.SG), currentSt.Stratum_CN)))
        if currentSG == None:
            currentSG = SampleGroupDO(dal)
            currentSG.Code = str.strip(row.SG)
            currentSG.CutLeave = row.CL
            currentSG.UOM = row.UOMP
            currentSG.PrimaryProduct = row.ProdP
            currentSG.SecondaryProduct = row.ProdS
            currentSG.DefaultLiveDead = row.LD
            currentSG.SamplingFrequency = getattrInt(row, "Freq")
            currentSG.KZ = getattrInt(row, "KZ")
            currentSG.Description = row.Description
            currentSG.Stratum = currentSt
			#if default live dead is null or empty
            if not currentSG.DefaultLiveDead:
                currentSG.DefaultLiveDead = "L" #fill in "L" as default
            currentSG.Save()
            log.lg('low', 'Created SG Record :' + str(currentSG.rowID))

        currentTDV = dal.ReadSingleRow[TreeDefaultValueDO]('TreeDefaultValue', 
'''WHERE Species = ? 
AND PrimaryProduct = ? 
AND LiveDead = ? And Chargeable = ? ''', # AND CullPrimary = ? 
#AND HiddenPrimary = ? 
#AND CullSecondary = ?
 
#AND HiddenSecondary = ?
#AND Recoverable = ?

#AND ContractSpecies = ? 
#AND TreeGrade = ? 
#AND MerchHeightType = ? 

#AND MerchHeightLogLength = ?
#AND FormClass = ?
#AND BarkThicknessRatio = ?
#AND AverageZ = ?
Array[Object]((row.Sp, row.ProdP, row.LD, row.YC)) )
        
        if currentTDV == None:
            currentTDV = TreeDefaultValueDO(dal)
            currentTDV.Species = row.Sp
            currentTDV.Chargeable = row.YC
            currentTDV.PrimaryProduct = row.ProdP
            currentTDV.LiveDead = row.LD
            currentTDV.CullPrimary = getattrFloat(row, "CDefP")
            currentTDV.HiddenPrimary = getattrFloat(row, "HDefP")
            currentTDV.CullSecondary = getattrFloat(row, "CDefS")
            currentTDV.HiddenSecondary = getattrFloat(row, "HDefS")
            currentTDV.Recoverable = getattrFloat(row, "RecDefP")
            currentTDV.ContractSpecies = row.ContrSpec
            currentTDV.TreeGrade = row.TreeGrade
            currentTDV.MerchHeightType = row.MrchHtT
            currentTDV.MerchHeightLogLength = row.MrchHtLL
            currentTDV.FormClass = row.FC
            currentTDV.BarkThicknessRatio = getattrFloat(row, "DBHBTR")
            currentTDV.AverageZ = getattrFloat(row,"AvgZForm")
            currentTDV.Save()
            log.lg('low', 'Created TDV Record :' + str(currentTDV.rowID))
        
        currentSG.TreeDefaultValues.Add(currentTDV)
        currentSG.TreeDefaultValues.Save()


def readCountTable(vw, db):
    log.lg('norm','START reading count table')
    
    from CruiseDAL.DataObjects import CountTreeDO
    from CruiseDAL.DataObjects import SampleGroupDO
    from CruiseDAL.DataObjects import CuttingUnitDO
    from CruiseDAL.DataObjects import TallyDO
    from CruiseDAL.DataObjects import TreeDefaultValueDO
    
    for row in vw:
        unit = db.ReadSingleRow[CuttingUnitDO]("CuttingUnit", "WHERE Code = ?", Array[Object]((str.strip(row.CutUnit), )))
        if not unit:
            log.lg('high', 'unable to locate record for Cutting Unit in Count Table: ' + row.CutUnit)
        sg = db.ReadSingleRow[SampleGroupDO]("SampleGroup", "JOIN Stratum ON SampleGroup.Stratum_CN = Stratum.Stratum_CN WHERE SampleGroup.Code = ? AND Stratum.Code = ?", Array[Object]((str.strip(row.SG), str.strip(row.Stratum))))
        if not sg:
            log.lg('high', 'unable to locate record for Sample Group in Count Table SG Code: ' + row.SG + ' St Code: ' + row.Stratum)
        tdv = db.ReadSingleRow[TreeDefaultValueDO]("TreeDefaultValue", 
                                                   """JOIN SampleGroupTreeDefaultValue AS sgtdv 
                                                   ON TreeDefaultValue.TreeDefaultValue_CN = sgtdv .TreeDefaultValue_CN
                                                   WHERE sgtdv.SampleGroup_CN = ? and Species = ?""", Array[Object]((sg.SampleGroup_CN, row.Sp )))

        if not row.Key == '*':
            tally = db.ReadSingleRow[TallyDO]("Tally", "Where HotKey = ? AND Description = ?", Array[Object]((row.Key, row.Description)))
            if tally == None:
                tally = TallyDO(db)
                tally.Hotkey = row.Key if row.Key else '?'
                tally.Description = row.Description
                tally.Save()
            
         
        count = CountTreeDO(db)
        count.SampleGroup = sg
        count.CuttingUnit = unit
        count.TreeDefaultValue = tdv
        count.Tally = tally
        
        count.TreeCount = int(row.Count) if row.Count else 0
        count.SumKPI = int(row.SumKPI) if row.SumKPI else 0
        count.Save()
        log.lg('low','Created Record :' + str(count.rowID))
        
    
def readPlotTable(vw, db):
    log.lg('norm','START reading plot table')
    
    from CruiseDAL.DataObjects import StratumDO
    from CruiseDAL.DataObjects import CuttingUnitDO
    from CruiseDAL.DataObjects import PlotDO
    

    
    for row in vw:
        
        stratum = db.ReadSingleRow[StratumDO]("Stratum", "WHERE Code = ?", Array[Object]((str.strip(row.Stratum), )))
        if not stratum:
            log.lg('high', 'unable to locate record for stratum in Plot table St Code: ' + row.Stratum)
        unit = db.ReadSingleRow[CuttingUnitDO]('CuttingUnit', 'WHERE Code = ?', Array[Object]((str.strip(row.CutUnit), )))
        if not unit:
            log.lg('high', 'unable to locate record for Cutting Unit in Plot table Unit Code: ' + row.CutUnit)
        
        plot = PlotDO(db)
        plot.Stratum = stratum
        plot.CuttingUnit = unit
        plot.PlotNumber = long(row.Plot) if row.Plot else 0
        plot.Slope = getattrFloat(row, "SlopePct")
        plot.Aspect = row.Aspect 
        plot.IsEmpty = 'True' if row.NullPlot == 1 else 'False'
        plot.XCoordinate = getattrFloat(row, "XCoord") 
        plot.YCoordinate = getattrFloat(row, "YCoord")
        plot.ZCoordinate = getattrFloat(row, "ZCoord")
        plot.MetaData = row.MetaData
        plot.Remarks = row.Remark
        plot.Save()
        log.lg('low','Created Record :' + str(plot.rowID))
        
        
def readTreeTable(vw, db):
    log.lg('norm','START reading tree table, this may take a while')
    
    from CruiseDAL.DataObjects import CuttingUnitDO
    from CruiseDAL.DataObjects import StratumDO
    from CruiseDAL.DataObjects import PlotDO
    from CruiseDAL.DataObjects import SampleGroupDO
    from CruiseDAL.DataObjects import TreeDefaultValueDO
    from CruiseDAL.DataObjects import TreeDO
    from CruiseDAL.DataObjects import CountTreeDO
    
    numTrees = len(vw)
    tenPct = numTrees /10
    if tenPct < 1 :
        tenPct = 1
    counter = 0
    for row in vw:
        if (counter % tenPct) == 0:
            print str(counter/tenPct) + '0%'
        counter += 1
        
        unit = db.ReadSingleRow[CuttingUnitDO]("CuttingUnit", 'WHERE Code = ?', Array[Object]((str.strip(row.CutUnit), )))
        if not unit:
            log.lg('high', 'unable to locate record for Cutting Unit in Tree table Unit Code: ' + row.CutUnit)
        stratum = db.ReadSingleRow[StratumDO]('Stratum', 'WHERE Code = ?', Array[Object]((str.strip(row.Stratum), )))
        if not stratum:
            log.lg('high', 'unable to locate record for Stratum in Tree table St Code: ' + row.Stratum)
        
        
            
        
        plot = db.ReadSingleRow[PlotDO]('Plot', 'WHERE PlotNumber = ? AND CuttingUnit_CN = ?', Array[Object]((row.Plot, unit.CuttingUnit_CN)))
        if not row.Sp:
            plot.KPI = row.KPI
            plot.Save()
            continue
        sg = db.ReadSingleRow[SampleGroupDO]('SampleGroup', 'WHERE Code = ? AND Stratum_CN = ?', Array[Object]((str.strip(row.SG), stratum.Stratum_CN)))
        if not sg:
            log.lg('high', 'unable to locate record for Sample Group  in Tree table SG Code: ' + row.SG)
        if(sg.SecondaryProduct == "" or sg.SecondaryProduct == None):
            sg.SecondaryProduct = row.ProdS
        elif (sg.SecondaryProduct != "" or sg.SecondaryProduct != None) and sg.SecondaryProduct != row.ProdS:
            raise Exception("same SG different Secondary Product")
        
    
        
        #find a treeDefault for the tree
        tdv =  db.ReadSingleRow[TreeDefaultValueDO]("TreeDefaultValue", 
                                                   """JOIN SampleGroupTreeDefaultValue AS sgtdv 
                                                   ON TreeDefaultValue.TreeDefaultValue_CN = sgtdv .TreeDefaultValue_CN
                                                   WHERE sgtdv.SampleGroup_CN = ? and Species = ? AND Chargeable = ?""", Array[Object]((sg.SampleGroup_CN, row.Sp, row.YC )))
        if not tdv:
            tdv = db.ReadSingleRow[TreeDefaultValueDO]("TreeDefaultValue", 
                                                    """JOIN SampleGroupTreeDefaultValue AS sgtdv 
                                                    ON TreeDefaultValue.TreeDefaultValue_CN = sgtdv .TreeDefaultValue_CN
                                                    WHERE sgtdv.SampleGroup_CN = ? and Species = ?""", Array[Object]((sg.SampleGroup_CN, row.Sp )))


        
        if row.MrchHtT == "L" and (not tdv.MerchHeightType or row.MrchHtT != tdv.MerchHeightType):
            #set tdv to row value if it isn't blank otherwise "F"
            tdv.MerchHeightType = row.MrchHtT 
            tdv.MerchHeightLogLength = row.MrchHtLL if row.MrchHtLL and row.MrchHtLL != 0 else 16
            tdv.Save()
        
        if not tdv.CullPrimary and row.CDefP:
            tdv.CullPrimary = getattrFloat(row ,"CDefP")
            tdv.Save()

        if tdv.Chargeable != row.YC:  
            try:
                copytdv = TreeDefaultValueDO(db)
                copytdv.SetValues(tdv)
                copytdv.Chargeable = row.YC
                copytdv.Save()
                tdv = copytdv
            except: 
                pass
            
        
        
        if stratum.Method == "3P" and row.CM == "M":
            count = db.ReadSingleRow[CountTreeDO]("CountTree", "WHERE SampleGroup_CN = ? AND CuttingUnit_CN = ?", Array[Object]((sg.SampleGroup_CN, unit.CuttingUnit_CN )))
            if count:
                count.SumKPI += row.KPI
                count.Save()
        #end 
        
        
                
        
        tree = TreeDO(db)
        tree.Stratum = stratum
        tree.CuttingUnit = unit
        tree.Plot = plot
        tree.SampleGroup = sg
        tree.TreeDefaultValue = tdv
        
        tree.TreeNumber = getattrInt(row, "Tree")		
        tree.STM = row.STM 
        tree.Species = row.Sp
        tree.CountOrMeasure = row.CM
        tree.TreeCount = row.TreeCnt
        tree.KPI = row.KPI
        tree.HiddenPrimary = getattrFloat(row ,"HDefP")
        tree.SeenDefectPrimary = getattrFloat(row ,"SDefP")
        tree.SeenDefectSecondary = getattrFloat(row ,"SDefS")
        tree.RecoverablePrimary = getattrFloat(row ,"RecDefP")
        tree.Initials = row.Initials
        tree.LiveDead = row.LD
        tree.Grade = row.TreeGrade
        tree.HeightToFirstLiveLimb = row.HgtFLL
        tree.PoleLength = row.PoleLen
        tree.ClearFace = row.Clear
        tree.CrownFratio = row.CR
        tree.DBH = getattrFloat(row ,"DBH")
        tree.DRC = getattrFloat(row ,"DRCOB")
        tree.TotalHeight = getattrFloat(row ,"TotHt")
        tree.MerchHeightPrimary = getattrFloat(row ,"MrchHtP")
        tree.MerchHeightSecondary = getattrFloat(row ,"MrchHtS")
        tree.FormClass = row.FC
        tree.UpperStemDOB = getattrFloat(row ,"UStemDOB") 
        tree.UpperStemHeight = getattrFloat(row ,"HgtUStem")
        tree.DBHDoubleBarkThickness = getattrFloat(row ,"DBHDBT") 
        tree.TopDIBPrimary = getattrFloat(row ,"TopDIBP")
        tree.TopDIBSecondary = getattrFloat(row ,"TopDIBS")
        tree.DefectCode = row.DefectCode
        tree.DiameterAtDefect = getattrFloat(row ,"DiamDefPt")
        tree.VoidPercent = getattrFloat(row, "VoidPct")
        tree.Remarks = row.Remarks
        tree.Save()
        #print('Created  Record :' + sale.rowID)
        
    
def readLogTable(vw, db):
    log.lg('norm','START reading log table, this may take a while')
    
    from CruiseDAL.DataObjects import LogDO
    from CruiseDAL.DataObjects import TreeDO
     
     
    numLogs = len(vw)
    tenPct = numLogs /10
    if tenPct < 1 :
        tenPct = 1
    counter = 0  
    for row in vw:
        
        if (counter % tenPct) == 0:
            print str(counter/tenPct) + '0%'
        counter += 1
        
        plotNum = row.Plot
        if not plotNum:
            tree = db.ReadSingleRow[TreeDO]('Tree', '''JOIN Stratum ON Tree.Stratum_CN = Stratum.Stratum_CN 
                JOIN CuttingUnit ON Tree.CuttingUnit_CN = CuttingUnit.CuttingUnit_CN 
                WHERE Tree.TreeNumber = ? 
                AND CuttingUnit.Code = ? 
                AND Stratum.Code = ?''', Array[Object]((row.Tree, str.strip(row.CutUnit), str.strip(row.Stratum))))
        else:
#             print repr(plotNum)
            tree = db.ReadSingleRow[TreeDO]('Tree', '''JOIN Stratum ON Tree.Stratum_CN = Stratum.Stratum_CN 
                JOIN CuttingUnit ON Tree.CuttingUnit_CN = CuttingUnit.CuttingUnit_CN 
                JOIN Plot ON Tree.Plot_CN = Plot.Plot_CN
                WHERE Tree.TreeNumber = ? 
                AND CuttingUnit.Code = ? 
                AND Stratum.Code = ?
                AND Plot.PlotNumber = ?''', Array[Object]((row.Tree, str.strip(row.CutUnit), str.strip(row.Stratum), row.Plot)))
        if not tree:
            log.lg('high', 'unable to locate Tree record in log table Tree num: ' + row.Tree + ' Unit Code: ' + row.CutUnit + ' St Code: ' + row.Stratum + ' Plot Num: ' + row.Plot)
            continue
        
        lg = LogDO(db)
        if getattrInt(row, 'FBSFlag') != tree.IsFallBuckScale: 
			if tree.IsFallBuckScale: 
				log.lg('norm','replacing FBSFlag on tree with' + getattrInt(row, 'FBSFlag'))
			tree.IsFallBuckScale = getattrInt(row, 'FBSFlag')
			tree.Save()
        lg.Tree = tree
        
        lg.LogNumber = row.LogNum
        lg.Grade = row.Grade
        
        lg.SeenDefect = getattrFloat(row, "PctSeenDef")
        
        
        lg.PercentRecoverable = getattrFloat(row, "PctRecChip")
        lg.Length = row.Length
        lg.ExportGrade = row.Sort
        lg.SmallEndDiameter = row.SErD
        lg.LargeEndDiameter = row.LErD
        
        lg.GrossBoardFoot = getattrFloat(row, "GBDFT") 
        
        lg.NetBoardFoot = getattrFloat(row, "NBDFT") 
        lg.GrossCubicFoot = getattrFloat(row, "GCUFT")
        lg.NetCubicFoot = getattrFloat(row, "NCUFT")
        lg.BoardFootRemoved = getattrFloat(row, "BDFTRem")
        lg.CubicFootRemoved = getattrFloat(row, "CUFTRem")
        lg.DIBClass = getattr(row, "DIBCls", 0.0) #missing field in some mk files
        lg.BarkThickness = getattrFloat(row, "DBT")
        lg.Save()
        
    
def readVoumeEquTable(vw, db):
    log.lg('norm','START reading volume table')
    
    from CruiseDAL.DataObjects import VolumeEquationDO

    for row in vw:
        
        eq = VolumeEquationDO(db)
        eq.Species = row.VolEqSpecie
        eq.PrimaryProduct = row.VolEqPP
        eq.VolumeEquationNumber = row.VolEqNum
        eq.StumpHeight = getattrFloat(row, "VolEqStump")
        eq.TopDIBPrimary = getattrFloat(row, "VolEqTopDIBP")
        eq.TopDIBSecondary = getattrFloat(row, "VolEqTopDIBS")
        
        flags = getattr(row, 'VolEqFlags')
        flags = list(flags)#get a list of the charaters in flags
        calcTotal = int(flags[0])
        calcBoard = int(flags[1])
        calcCubic = int(flags[2])
        calcCords = int(flags[3])
        calcTopwood = int(flags[4])
        
        eq.CalcTotal = calcTotal
        eq.CalcBoard = calcBoard
        eq.CalcCubic = calcCubic
        eq.CalcCord = calcCords
        eq.CalcTopwood = calcTopwood
        
        eq.Save()
        

    
def readGlobalConfigTable(vw, db):
    log.lg('norm','START reading global config table')
    
    from CruiseDAL.DataObjects import GlobalsDO
    from CruiseDAL.DataObjects import ReportsDO
    
    for row in vw:
        if(getattr(row,"Key") == "Reports"): #special condition 
            rpt = ReportsDO(db)
            rpt.ReportID = row.Value
            rpt.Selected = 1
            rpt.Title = ''
            rpt.Save()
        else:
            g = GlobalsDO(db)
            g.Block = row.Block
            g.Key = row.Key
            g.Value = row.Value
            try:
                g.Save()
                pass
            except Exception as e:
                log.lg('high', 'unable to convert global rec Key:' + str(row.Key) + '|' + e.ToString())
                pass
            
        
        
    
        
def readMessageLogTable(vw, db):
    log.lg('norm','START reading message log table')
    
    from CruiseDAL.DataObjects import MessageLogDO
    
    for row in vw:
        msg = MessageLogDO(db)
        msg.Message = row.Msg
        msg.Date = row.Date
        msg.Time = row.Time
        msg.Level = row.Level
        msg.Save()
        
    
def readWeightEquationTable(vw, db):
    log.lg('norm','START reading weight equation table')
    

    from CruiseDAL.DataObjects import BiomassEquationDO
    from CruiseDAL.DataObjects import WeightEquationDO 
    bioPropPrefix = ['BioEq', 'BioMoist', 'BioRemv']
    bioPropSuffix = ['Fol', 'LBr', 'DBr', 'TotTree']
    
    for row in vw: 
        wEQ = WeightEquationDO(db)
        wEQ.Species = row.WgtEqSpecie
        wEQ.PrimaryProduct = row.WgtEqPP
        wEQ.LiveDead = row.WgtEqLiveDead
        wEQ.WeightFactorPrimary = getattrFloat(row, "WgtEqFactor")
        wEQ.WeightFactorSecondary = getattrFloat(row, "WgtEqFactor2")
        wEQ.PercentRemovedPrimary = getattrFloat(row, "WgtEqPercent")
        eEQ.PercenRemovedSecondary = getattrFloat(row, "WgtEqPercent2")
        
        
        for suffix in bioPropSuffix:
            if hasattr(row,bioPropPrefix[0] + suffix) and not getattr(row, bioPropPrefix[0] + suffix) == 0:
                
                bio = BiomassEquationDO(db)
                bio.Species = row.WgtEqSpecie
                bio.Product = row.BioPr
                bio.Component = suffix
                bio.Equation = getattr(row, 'BioEq' + suffix)
                bio.PercentMoisture = getattrFloat(row, 'BioMoist' + suffix)
                bio.PercentRemoved = getattrFloat(row, 'BioRemv' + suffix)
                bio.Save()

        



def readValueEquationTable(vw, db):
    log.lg('norm', 'START  reading value equation table')
    

    from CruiseDAL.DataObjects import ValueEquationDO
    
    
    for row in vw:
        valEq = ValueEquationDO(db)
        valEq.Species = row.ValEQSpecie
        valEq.PrimaryProduct = row.ValEqPP
        valEq.ValueEquationNumber = row.ValEqNum
        valEq.Grade = row.ValEqGrade 
        valEq.Coefficent1 = getattrFloat(row, "ValEqCoef1")
        valEq.Coefficient2 = getattrFloat(row, "ValEqCoef2")
        valEq.Coefficient3 = getattrFloat(row, "ValEqCoef3")
        valEq.Coefficient4 = getattrFloat(row, "ValEqCoef4")
        valEq.Coefficient5 = getattrFloat(row, "ValEqCoef5")
        valEq.Coefficient6 = getattrFloat(row, "ValEqCoef6")
        valEq.Save()
        
        
    
def readQAEquationTable(vw, db):
    log.lg('norm', 'START reading QAEquation table')
    
    
    from CruiseDAL.DataObjects import QualityAdjEquation
    

    
    for row in vw:
        qual = QualityAdjEquationDO(db)
        qual.Species = row.QaEqSpecie
        qual.QualityAdjEq = row.QaEqNum
        qual.Year = row.QaEqYear
        qual.Grade = row.QaEqGrade
        qual.Coefficient1 = getattrFloat(row, "QaEqCoef1")
        qual.Coefficient2 = getattrFloat(row, "QaEqCoef2")
        qual.Coefficient3 = getattrFloat(row, "QaEqCoef3")
        qual.Coefficient4 = getattrFloat(row, "QaEqCoef4")
        qual.Coefficient5 = getattrFloat(row, "QaEqCoef5")
        qual.Coefficient6 = getattrFloat(row, "QaEqCoef6")
        qual.Save()
        

    

    
    
