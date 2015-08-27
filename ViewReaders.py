'''
Created on Jun 30, 2011

@author: benjaminjcampbell



'''
import collections
import Logger

log = Logger.Logger()



createdBy = 'COConver Utility'
# createdDate = ''#'current_date'

# import TableManager
# tableManager = TableManager.TableManager()

#function InsertData:
#builds and executes sql insert statments to insert data into sql tables 
#takes tableName - name of the sql table to insert data into
#      fieldNames - list of sql columns that the data will be inseted into
#      dataList - data to insert, data must be in same order as fieldNames
#      cursor - db cursor object

# def insertData(tableName, fieldNames, dataList, cursor):
#     for data in dataList:
#         
#         valueString = []
#         for v in data:
#             if isinstance(v,str): #if value is a string
#                 if v == 'current_date':
#                     valueString.append(v)
#                 else:                
#                     v = v.replace("'", "''")
#                     valueString.append("'{0}'".format(v))#add single quotes
#             else:
#                 if(v == None):
#                     valueString.append('NULL')
#                 else:
#                     valueString.append(str(v))
#         valueString = ','.join(valueString)
#         
#         command = 'insert into {0}({1}) values ({2});'.format(tableName, ','.join(fieldNames), valueString)
#         log.lg('low', command)
#         cursor.execute(command)

#function getKeyValues:
#helper function for retrieving key data form a metakit view
#takes:  row - the metakit row to retriev the data from 
#        keyPropertys - a list containg strings itentefying the mk props to retrieve data from
#        keyConstructer = optional arg takes the data type to insert the data into
#                         in most cases this will be a namedtuple customized for the key
# def getKeyValues(row, keyPropertys, keyConstructer = tuple):
#     values = []
#     for propName in keyPropertys:
#         values.append(getattr(row, propName))
#     if keyConstructer == tuple:
#         return keyConstructer(values)
#     else:
#         return keyConstructer(*values)

# #Below are groups of table key namedtuples, table fields lists, table data namedtuples and table propertys lists
# #table key namedtuples are intended to store data from rows that allow forgen keys to be resolved to that row's data and behave like a struct in C#
# #table field lists store a list of ordered sql field names for the coresponding table
# #table data namedtuples store all the data for each sql field for each row and contain data members for each field in the table's coresponding data field list
# #table propertys list is a list of metakit propertys that need to be accessed to populate SOME of the table fields *
# # *note the order of items in the property list should match the order of the corespondeing fields in the table fields list and
# #    fields not generated directaly from the property list (such as forgen keys) should should be at the end or beginning of the table field list, not mix in
# 
# SaleTableKey = collections.namedtuple('SaleTableKey', 'SaleNo')
# saleTableFields = 'SaleNumber Name Purpose Region Forest District CalendarYear Remarks CreatedBy CreatedDate'
# SaleTableData = collections.namedtuple('SaleTableData', saleTableFields)
# saleTablePropertys = 'SaleNo SaleName Purpose Region Forest District CalYear Remarks'.split()
# 
# #CruiseTableKey = collections.namedtuple('CruiseTableKey', 'CruiseNo')
# #cruiseTableFields = 'Sale_CN CruiseNumber Purpose CruiseType CreatedBy CreatedDate'
# #CruiseTableData = collections.namedtuple('CruiseTableData', cruiseTableFields)
# #cruiseTablePropertys = 'CruiseNo Purpose CruiseType'.split()
# 
# cuttingUnitKeyPropertys = ['CutUnit']
# CuttingUnitKey = collections.namedtuple('CuttingUnitKey', 'CutUnit')
# cuttingUnitFields = 'Code Area Description LoggingMethod PaymentUnit CreatedBy CreatedDate'
# CuttingUnitData = collections.namedtuple('CuttingUnitData', cuttingUnitFields)
# cuttingUnitPropertys = 'CutUnit Area Description LogMeth PayUnit'.split()
# 
# stratumKeyPropertys = 'Stratum'
# StratumKey = collections.namedtuple('StratumTableKey', stratumKeyPropertys)
# stratumFields = 'Code Description Method BasalAreaFactor FixedPlotSize Month Year CreatedBy CreatedDate'
# StratumData = collections.namedtuple('StratumTableData', stratumFields)
# stratumPropertys = 'Stratum Description CruzMeth BAF FPSize Month Year'.split()
# 
# cutUnitStratumFields = 'CuttingUnit_CN Stratum_CN'
# CutUnitStratumMap = collections.namedtuple('CutUnitStratumMap', 'CuttingUnit_CN Stratum_CN')
# 
# sampleGroupDefaultFields = 'TreeDefaultValue_CN SampleGroup_CN'
# SampleGroupDefaultMap = collections.namedtuple('SampleGroupDefaultMap', sampleGroupDefaultFields)
# sampleGroupDefaultKeyPropertys = 'Stratum SG Sp'
# SampleGroupDefaultKey = collections.namedtuple('SampleGroupDefaultKey', sampleGroupDefaultKeyPropertys)
# 
# sampleGroupFields = 'Stratum_CN Code CutLeave UOM PrimaryProduct SecondaryProduct DefaultLiveDead SamplingFrequency KZ Description CreatedBy CreatedDate'
# SampleGroupData = collections.namedtuple('SampleGroupData', sampleGroupFields)
# sgDataPropertys = 'SG CL UOMP ProdP ProdS LD Freq KZ Description'.split()
# sampleGroupKeyPropertys = 'SG Stratum'
# SampleGroupKey = collections.namedtuple('SampleGroupKey', sampleGroupKeyPropertys)
# 
# treeDefaultPropertys = 'Sp ProdP LD CDefP HDefP CDefS HDefS RecDefP ContrSpec TreeGrade MrchHtT MrchHtLL FC DBHBTR AvgZForm'
# TreeDefaultData = collections.namedtuple('TreeDefaultData', treeDefaultPropertys)
# TreeDefaultKey = collections.namedtuple('TreeDefaultKey', treeDefaultPropertys)
# treeDefaultFields = 'Species PrimaryProduct LiveDead CullPrimary HiddenPrimary CullSecondary HiddenSecondary Recoverable ContractSpecies TreeGrade MerchHeightType MerchHeightLogLength FormClass BarkThicknessRatio AverageZ'.split()
# 
# 
# 
# tallyKeyPropertys = 'Key Description'
# TallyKey = collections.namedtuple('TallyKey', tallyKeyPropertys)
# tallyFields = 'HotKey Description'
# 
# countTreeKeyPropertys = 'CutUnit Stratum SG Sp'
# CountTreeKey = collections.namedtuple('CountTreeKey', countTreeKeyPropertys)
# countTreesFields = 'SampleGroup_CN CuttingUnit_CN Tally_CN TreeDefaultValue_CN TreeCount SumKPI CreatedBy CreatedDate'#removed species_3p
# CountTreesData = collections.namedtuple('CountTreesData', countTreesFields)
# #countTreesPropertys = ...
# 
# plotKeyPropertys ='Stratum CutUnit Plot'
# PlotKey = collections.namedtuple('PlotKey', 'Stratum CutUnit Plot')
# plotDataFields = 'Stratum_CN CuttingUnit_CN PlotNumber Slope Aspect IsEmpty XCoordinate YCoordinate ZCoordinate MetaData Remarks CreatedBy CreatedDate'
# PlotData = collections.namedtuple('PlotData', plotDataFields)
# plotDataPropertys = 'Plot SlopePct Aspect NullPlot XCoord YCoord ZCoord MetaData Remark'.split()
# 
# treeKeyPropertys = 'Stratum CutUnit Plot Tree'
# TreeKey = collections.namedtuple('TreeKey', treeKeyPropertys)
# treeDataFields = '''TreeDefaultValue_CN Stratum_CN SampleGroup_CN CuttingUnit_CN Plot_CN 
#     TreeNumber STM Species CountOrMeasure TreeCount 
#     KPI SeenDefectPrimary SeenDefectSecondary RecoverablePrimary 
#     Initials LiveDead Grade HeightToFirstLiveLimb PoleLength ClearFace 
#     CrownRatio DBH DRC TotalHeight MerchHeightPrimary MerchHeightSecondary 
#     FormClass UpperStemDOB UpperStemHeight DBHDoubleBarkThickness 
#     TopDIBPrimary TopDIBSecondary DefectCode DiameterAtDefect VoidPercent Remarks CreatedBy CreatedDate'''
# TreeData = collections.namedtuple('TreeData', treeDataFields)
# treeDataPropertys = '''Tree STM Sp CM TreeCnt KPI SDefP SDefS RecDefP 
#     Initials LD TreeGrade HgtFLL PoleLen Clear CR DBH DRCOB TotHt MrchHtP 
#     MrchHtS FC UStemDOB HgtUStem DBHDBT TopDIBP TopDIBS DefectCode
#     DiamDefPt VoidPct Remarks'''.split()
# 
# logKeyPropertys = 'Stratum CutUnit Plot Tree LogNum'.split()    
# logDataFields = 'Tree_CN LogNumber Grade SeenDefect PercentRecoverable Length ExportGrade SmallEndDiameter LargeEndDiameter GrossBoardFoot NetBoardFoot GrossCubicFoot NetCubicFoot BoardFootRemoved CubicFootRemoved DIBClass BarkThickness CreatedBy CreatedDate'
# LogData = collections.namedtuple('LogData', logDataFields)
# logDataPropertys = 'LogNum Grade PctSeenDef PctRecChip Length Sort SErD LErD GBDFT NBDFT GCUFT NCUFT BDFTRem CUFTRem DIBCls DBT'.split()
# 
# volumeEquationKey = 'VolEqSpecie VolEqPP VolEqNum'.split()
# volumeEquationFields = 'Species PrimaryProduct VolumeEquationNumber StumpHeight TopDIBPrimary TopDIBSecondary CalcTotal CalcBoard CalcCubic CalcCord CalcTopWood'
# VolumeEquationData = collections.namedtuple('VolumeEquationData', volumeEquationFields)
# volumeEquationPropertys = 'VolEqSpecie VolEqPP VolEqNum VolEqStump VolEqTopDIBP VolEqTopDIBS'.split()
# 
# #global config has no unique constraints so im not going to bother with a key for it
# globalConfigFields = 'Block Key Value'
# globalConfigPropertys = globalConfigFields
# GlobalConfigData = collections.namedtuple('GlobalConfigData', globalConfigFields)
# 
# #no unique/no key
# messageLogFields = 'Message Date Time Level'
# MessageLogData = collections.namedtuple('MessageLogData', messageLogFields)
# messageLogPropertys = 'Msg Date Time Level'.split()
# 
# #this table is a little strange, look at readWeightEquationTable to see how im doing keys
# weightEquationFields = 'Species PrimaryProduct LiveDead WeightFactorPrimary WeightFactorSecondary PercentRemovedPrimary PercentRemovedSecondary'
# WeightEquationData = collections.namedtuple('WeightEquationData', weightEquationFields)
# weightEquationPropertys = 'WgtEqSpecie WgtEqPP WgtEqLiveDead WgtEqFactor WgtEqFactor2 WgtEqPercent WgtEqPercent2'
# 
# bioEquationFields = 'Species Product Component Equation PercentMoisture PercentRemoved'
# BioEquationData = collections.namedtuple('BioEquationData', bioEquationFields)
# 
# valueEquationPropertys = 'ValEQSpecie ValEqPP ValEqNum ValEqGrade ValEqCoef1 ValEqCoef2 ValEqCoef3 ValEqCoef4 ValEqCoef5 ValEqCoef6'
# valueEquationFields = 'Species PrimaryProduct ValueEquationNumber Grade Coefficient1 Coefficient2 Coefficient3 Coefficient4 Coefficient5 Coefficient6'
# ValueEquationData = collections.namedtuple('ValueEquationData', valueEquationFields)  
# 
# qaEquationPropertys = 'QaEqSpecie QaEqNum QaEqYear QaEqGrade QaEqCoef1 QaEqCoef2 QaEqCoef3 QaEqCoef4 QaEqCoef5 QaEqCoef6'
# qualityAdjEquationFields = 'Species QualityAdjEq Year Grade Coefficient1 Coeffiecient2 Coefficient3 Coefficient4 coefficient5 Coeffieient6' 
# QAEquationData = collections.namedtuple('QAEquationData', qualityAdjEquationFields)
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
def getattrFloat(source, attr, e = 2.3283064e-10, max = 2000000):
    value = None
    try:
        value = getattr(source, attr)
        if not isinstance(value, float):
            value = float(value)
    except:
        log.lg('low',"overriding value {0} on property {1} with 0.0 (float)".format(repr(value), attr))
        value = 0.0
        
    
        
    if (value != 0.0 and (abs(value) < e or abs(value) > max)):
        log.lg("high","overriding value {0} on property {1} with 0.0 (float)".format(repr(value), attr))
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
        log.lg("low","overriding value {0} on property {1} with 0 (int)".format(repr(value), attr))
        value = 0
        pass
    
    return value


    
    


def readCruiseTable(vw, dal):
    
    from CruiseDAL.DataObjects import SaleDO
    log.lg('norm','START reading cruise table')
    
    for row in vw:
        sale = SaleDO(dal)
        sale.SaleNumber = getattr(row,'SaleNo')
        sale.Name = row.SaleName
        sale.Purpose = row.Purpose
        sale.Region = row.Region
        sale.Forest = row.Forest
        sale.District = row.District
        sale.CalendarYear = getattrInt(row, 'CalYear')
        sale.Remarks = row.Remarks
        sale.Save()
        log.lg('low','Created Record :' + str(sale.rowID))
        
        

        
def readCuttingUnitsTable(vw, dal):
    from CruiseDAL.DataObjects import CuttingUnitDO
    log.lg('norm','START reading cuttingunits table')


    for row in vw:
        unit = CuttingUnitDO(dal)
        unit.Code = str.strip(row.CutUnit)
        unit.Area = getattrFloat(row, "Area")
        unit.Description = row.Description
        unit.LoggingMethod = row.LogMeth
        unit.PaymentUnit = row.PayUnit
        unit.Save()
        log.lg('low','Created Record :' + str(unit.rowID))

#         
        
def readStratumTable(vw, dal):

    log.lg('norm','START reading stratum table')
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
        log.lg('low','Created Record :' + str(stratum.rowID))
        unitCodes = row.Units.split(',')
        for c in unitCodes:
            prams = Array.CreateInstance(Object, 1)
            prams[0] = str.strip(c)
            unit = dal.ReadSingleRow[CuttingUnitDO]('CuttingUnit', 'WHERE Code = ?', prams )
            if not unit: 
                log.lg('high', 'unable to locate Cutting Unit record in Stratum table. Unit Code: ' + c)
            stratum.CuttingUnits.Add(unit)
        stratum.CuttingUnits.Save()

            
        

#         #store cruzMeth for later use 
#         tableManager.setTag('Stratum', currentStTK, getattr(row,'CruzMeth'))
#         

#         for k in getattr(row, 'Units').split(','):
#             k = str.strip(k)                                                #remove excess white space
#             key = CuttingUnitKey(k)                                         #make a cutting unit key
#             cutUnitIndex = tableManager.getKeyIndex('CuttingUnit', key)     #find corresponding cutting unit index
#             cutUnitStratumMaps.append(CutUnitStratumMap(cutUnitIndex, stratumIndex))
#         

        
    
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
            log.lg('low','Created SG Record :' + str(currentSG.rowID))
        

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
            currentTDV.HiddenSecondary = getattrFloat(row ,"HDefS")
            currentTDV.Recoverable = getattrFloat(row ,"RecDefP")
            currentTDV.ContractSpecies = row.ContrSpec 
            currentTDV.TreeGrade = row.TreeGrade
            currentTDV.MerchHeightType = row.MrchHtT
            currentTDV.MerchHeightLogLength = row.MrchHtLL
            currentTDV.FormClass = row.FC
            currentTDV.BarkThicknessRatio = getattrFloat(row, "DBHBTR")
            currentTDV.AverageZ = getattrFloat(row ,"AvgZForm")
            currentTDV.Save()
            log.lg('low','Created TDV Record :' + str(currentTDV.rowID))
        
        currentSG.TreeDefaultValues.Add(currentTDV)
        currentSG.TreeDefaultValues.Save()
     
#         currentSGKIndex = None
#         if tableManager.hasKey('SampleGroup', currentSGK) == True:
#             currentSGKIndex= tableManager.getKeyIndex('SampleGroup', currentSGK)
#         else:
#             currentSGKIndex = tableManager.addKeyIndex('SampleGroup', currentSGK)
#             
#             values = []
#             stratumKey = StratumKey(getattr(row,'Stratum'))
#             values.append(tableManager.getKeyIndex('Stratum', stratumKey))
#             for propName in sgDataPropertys:
#                 if(propName == 'ProdP' and getattr(row, propName) == None ):
#                     values.append('02') # if primary product not used default to 02
#                 else:
#                     values.append(getattr(row, propName))
#             values.append(createdBy)
#             values.append(createdDate)
#             sgData.append(SampleGroupData(*values))
#             
#         #HACK because some types in the TreeDefault table dont match the types in metakit 
#         #a special case must be made
#         currentTDK = getKeyValues(row, treeDefaultPropertys.split(), TreeDefaultKey)
#         values = []
#         for propName in treeDefaultPropertys.split():
#             if propName in {'CDefP', 'HDefP', 'CDefS', 'HDefS', 'RecDefP'}:
#                 value = getattr(row, propName)
#                 if value == '':
#                     value = None
#                 else:
#                     value = float(value)
#                 values.append(value)
#             else:
#                 values.append(getattr(row, propName))
#         if(tableManager.hasKey('TreeDefaults', currentTDK) == False):
#             tdData.append(TreeDefaultData(*values))
#             currentTDKIndex = tableManager.addKeyIndex('TreeDefaults', currentTDK, False)
#         else:
#             currentTDKIndex = tableManager.getKeyIndex('TreeDefaults', currentTDK)
#         
#         #add currenSGK / currentTDK pair to samplegroupDefaults set 
#         currentSGTDVK = getKeyValues(row, sampleGroupDefaultKeyPropertys.split(), SampleGroupDefaultKey)
#         currentSGTDVData = SampleGroupDefaultMap( currentTDKIndex, currentSGKIndex)
#         sgDefaultMaps.add( currentSGTDVData)
#         tableManager.addKeyIndex('SampleGroupDefault', currentSGTDVK)
#         tableManager.setTag('SampleGroupDefault', currentSGTDVK, currentSGTDVData)
#               


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
        
        
#         countTreeKey = getKeyValues(row, countTreeKeyPropertys.split(), CountTreeKey)
#         
#         countTreeKeys.append(countTreeKey)
#         
#         currentSGK = getKeyValues(row, sampleGroupKeyPropertys.split(), SampleGroupKey)
#         currentSGKIndex = tableManager.getKeyIndex('SampleGroup', currentSGK)
#         
#         currentCUTK = getKeyValues(row, cuttingUnitKeyPropertys, CuttingUnitKey)
#         currentCUTKIndex = tableManager.getKeyIndex('CuttingUnit', currentCUTK)
#         
#         #try to get the TreeDefaultValue_CN
#         try:
#             currentSGTDVK = getKeyValues(row, sampleGroupDefaultKeyPropertys.split(), SampleGroupDefaultKey)
#             currentTDKIndex = tableManager.getTag('SampleGroupDefault', currentSGTDVK).TreeDefaultValue_CN
#         except:
#             currentTDKIndex = None
#             
#         #all data going into Tally will need to be unique 
#         #so we will use the key as the data too
#         currentTallyKey = getKeyValues(row, tallyKeyPropertys.split(), TallyKey)
#         if(not getattr(row,'Key') == '*'):
#             currentTallyKeyIndex = tableManager.addKeyIndex('Tally', currentTallyKey, True)
#         else:
#             currentTallyKeyIndex = None
#             
#         #this is a special case can this be fixed 
#         values = []
#         values.append(currentSGKIndex)
#         values.append(currentCUTKIndex)
#         values.append(currentTallyKeyIndex)
#         values.append(currentTDKIndex)
#         values.append(getattr(row,'Count'))#this value is stored as a long and is giving problems, this is why we are extracting data manualy here.
#         values.append(int(getattr(row,'SumKPI')))#and i think this is a long too.
#         values.append(createdBy)
#         values.append(createdDate)
#         
#         tempCountTreeLookupKey = (currentSGKIndex, currentCUTKIndex)
#         if not tempCountTreeLookup.has_key(tempCountTreeLookupKey):
#             tableManager.addKeyIndex('CountTree', countTreeKey, True)
#             tempCountTreeLookup[tempCountTreeLookupKey] = [values, ]
#         elif getattr(row, "Key") == "*":
#             assert len(tempCountTreeLookup[tempCountTreeLookupKey]) == 1
#             tempCountTreeLookup[tempCountTreeLookupKey][0][3] = None
#         elif not getattr(row, "Key") == "*":
#             tempCountTreeLookup[tempCountTreeLookupKey].append(values)
#             tableManager.addKeyIndex('CountTree', countTreeKey, True)
#             
#         
#             
#         #
# #        for propName in countTreesPropertys:          
# #            values.append(getattr(row, propName))
#         #countTreesData.append(CountTreesData(*values))
#     
#     for lst in tempCountTreeLookup.values():
#         for valueList in lst:
#             countTreesData.append(CountTreesData(*valueList))
#     
#     #if countTreeKeys has no item then no data was read
#     #so dont try to get keys for Tally
#     if len(countTreeKeys) > 0:
#         tallyKeys = tableManager.getOrderdKeys('Tally')
#         insertData('Tally', tallyFields.split(), tallyKeys, cursor)    
#     
#     insertData('CountTree', countTreesFields.split(), countTreesData, cursor)
    
    
    
    
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
        
#         plotKey = getKeyValues(row, plotKeyPropertys.split(), PlotKey)
#         plotKeys.append(plotKey)
#         
#         currentCUTK = getKeyValues(row, cuttingUnitKeyPropertys, CuttingUnitKey)
#         
#         currentStTK = StratumKey(getattr(row, stratumKeyPropertys))
#            
#         values = []
#         values.append(tableManager.getKeyIndex('Stratum', currentStTK))
#         values.append(tableManager.getKeyIndex('CuttingUnit', currentCUTK))
#         for propName in plotDataPropertys:
#             if propName in {'Slope', 'Aspect', 'XCoord', 'YCoord', 'ZCoord'}:
#                 value = getattr(row, propName)
#                 if value == '':
#                     value = None
#                 else:
#                     value = float(value)
#                 values.append(value)
#             else:
#                 values.append(getattr(row, propName))
#         values.append(createdBy)
#         values.append(createdDate)
#         plotData.append(PlotData(*values))
#         
#     tableManager.addKeyIndexs('Plot', plotKeys)
#         
#     insertData('Plot', plotDataFields.split(), plotData,cursor)
        
def readTreeTable(vw, db):
    log.lg('norm','START reading tree table, this may take a while')
    
#     treeKeys = []
#     treeData = []
#     treeKeyPropertys = 'Stratum CutUnit Plot Tree'
# TreeKey = collections.namedtuple('TreeKey', treeKeyPropertys)
# 
# treeDataFields = '''TreeDefaultValue_CN Stratum_CN SampleGroup_CN CuttingUnit_CN Plot_CN 
#     TreeNumber STM Species CountOrMeasure TreeCount 
#     KPI SeenDefectPrimary SeenDefectSecondary RecoverablePrimary 
#     Initials LiveDead Grade HeightToFirstLiveLimb PoleLength ClearFace 
#     CrownRatio DBH DRC TotalHeight MerchHeightPrimary MerchHeightSecondary 
#     FormClass UpperStemDOB UpperStemHeight DBHDoubleBarkThickness 
#     TopDIBPrimary TopDIBSecondary DefectCode DiameterAtDefect VoidPercent Remarks CreatedBy CreatedDate'''
# TreeData = collections.namedtuple('TreeData', treeDataFields)
# 
# treeDataPropertys = '''Tree STM Sp CM TreeCnt KPI SDefP SDefS RecDefP 
#     Initials LD TreeGrade HgtFLL PoleLen Clear CR DBH DRCOB TotHt MrchHtP 
#     MrchHtS FC UStemDOB HgtUStem DBHDBT TopDIBP TopDIBS DefectCode
#     DiamDefPt VoidPct Remarks'''
#     
#     
#     tempTDKIndexTable = dict()
#     tempSgIndexTable = dict()
    
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
#         tdv = db.ReadSingleRow[TreeDefaultValueDO]("TreeDefaultValue", 
#                                                    """JOIN SampleGroupTreeDefaultValue AS sgtdv 
#                                                    ON TreeDefaultValue.TreeDefaultValue_CN = sgtdv .TreeDefaultValue_CN
#                                                    WHERE sgtdv.SampleGroup_CN = ? and Species = ?""", Array[Object]((sg.SampleGroup_CN, row.Sp )))
        tdv =  db.ReadSingleRow[TreeDefaultValueDO]("TreeDefaultValue", 
                                                   """JOIN SampleGroupTreeDefaultValue AS sgtdv 
                                                   ON TreeDefaultValue.TreeDefaultValue_CN = sgtdv .TreeDefaultValue_CN
                                                   WHERE sgtdv.SampleGroup_CN = ? and Species = ? AND Chargeable = ?""", Array[Object]((sg.SampleGroup_CN, row.Sp, row.YC )))
#         for d in sg.TreeDefaultValues:
#             print d.TreeDefaultValue_CN
#             tdv = d
#         if tryTDVCorectYC:
#             tdv = tryTDVCorectYC 
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
        
        tree.TreeNumber = row.Tree
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
        
        
        
        
#         treeKey = getKeyValues(row, treeKeyPropertys.split(), TreeKey)
#         treeKeys.append(treeKey)
#         
#         currentStTK = StratumKey(getattr(row, stratumKeyPropertys))
#         currentStTKIndex = tableManager.getKeyIndex('Stratum', currentStTK)
#         
#         currentSGK = getKeyValues(row, sampleGroupKeyPropertys.split(), SampleGroupKey)
#         currentSGKIndex = tableManager.getKeyIndex('SampleGroup', currentSGK)
#         
#         currentCUTK = CuttingUnitKey(getattr(row,'CutUnit'))
#         currentCUTKIndex = tableManager.getKeyIndex('CuttingUnit', currentCUTK)
#         
#         currentPTK = getKeyValues(row, plotKeyPropertys.split(), PlotKey)
#         currentPTKIndex = tableManager.getKeyIndex('Plot', currentPTK)
#         
#         crzMeth = tableManager.getTag('Stratum', currentStTK)
#         
# #         if currentPTKIndex == 0: #WHAT? why am I creating plot records for tree based methods
# #             
# #             if crzMeth in ['STR', '3P', '100','S3P', '3 P']:
# #                 log.lg('norm', 'missing plot reference found, generating plot record')
# #                 currentPTKIndex = tableManager.addKeyIndex('Plot', currentPTK)
# #                 #'Stratum_CN CuttingUnit_CN PlotNumber Slope Aspect IsEmpty XCoordinate YCoordinate ZCoordinate MetaData Remarks CreatedBy CreatedDate'
# #                 newPTData = PlotData(currentStTKIndex, currentCUTKIndex, currentPTK.Plot,0,None,None,None,None,None,None,None, createdBy, '')
# #                 insertData('Plot', plotDataFields.split(), [newPTData],cursor)
#         
#         #specal condition: if a tree record can't be associated with a TDV, because it doesn't have a species
#         #update it's accosated plot with it's kpi value and dont create a tree record. 
#         #this is because plot kpi values were stored in the tree table
#         try:
#             currentSGTDVK = getKeyValues(row, sampleGroupDefaultKeyPropertys.split(), SampleGroupDefaultKey)
#             currentTDKIndex = tableManager.getTag('SampleGroupDefault', currentSGTDVK).TreeDefaultValue_CN
#         except: 
#             if getattr(row, 'Tree') == '0':
#                 updateStmt = 'UPDATE Plot set KPI = {kpiVal} WHERE rowid = {plot_cn};'.format(kpiVal = getattr(row, 'KPI'), plot_cn = currentPTKIndex)
#                 log.lg('low',updateStmt)
#                 cursor.execute(updateStmt)
#             continue # do not add tree to tree table 
#         
# #        currentCountTreeKey = getKeyValues(row, countTreeKeyPropertys.split(), CountTreeKey)
# #        currentCountTreeKeyIndex = tableManager.getKeyIndex('CountTree', currentCountTreeKey)
#         
#         if crzMeth in ['S3P', '3P', '3 P']:
#             currentCountTreeKey = getKeyValues(row, countTreeKeyPropertys.split(), CountTreeKey)
#             currentCountTreeKeyIndex = tableManager.getKeyIndex('CountTree', currentCountTreeKey)
#             kpiValue = int(getattr(row, 'KPI'))
#             #only if crzMeth == S3P?
#             treeEstimateData = [[kpiValue, currentCountTreeKeyIndex], ]
#             insertData('TreeEstimate','KPI CountTree_CN'.split(), treeEstimateData, cursor)
#             #create update statment that will add kpiValue to CountTree.KPI in database
#             updateStmt = 'UPDATE CountTree set SumKPI = SumKPI + ? WHERE CountTree_CN = ?;'
#             log.lg('low',updateStmt)
#             cursor.execute(updateStmt, treeEstimateData[0])
#             
#             if crzMeth == 'S3P' and getattr(row, 'CM') == 'C':
#                 continue # do not add tree to tree table 
#             
#             
# #            threePCode = getattr(row, '3Pcode')
# #            if threePCode == 3:
# #                threePSGK = currentSGK.replace(SG = '3P')
# #                if tableManager.hasKey(currentSGK) == False:
# #                    tableManager.addKeyIndex("SampleGroup", threePSGK)
# #                    tableManager.setTag("SampleGroup", threePSGK, getattr(row, "ProdP"))
# #                    #HACK 
# #                    cursor.execute('''INSERT OR FAIL INTO SampleGroup (Stratum_CN, Code, CutLeave, UOM, PrimaryProduct, SecondaryProduct, DefaultLiveDead)
# #                        SELECT Stratum_CN, :code, CutLeave, UOM, PrimaryProduct, SecondaryProduct, DefaultLiveDead  FROM SampleGroup
# #                        WHERE Stratum_CN = :str AND Code = :oldCode);''', str = currentStKIndex, code = currentSGK.SG )
# #                    currentSGKIndex = tableManager("SampleGroup", threepSGK)
# #                
# #
# #                else:
# #                    sqlStr = '''UPDATE SampleGroup Set PrimaryProduct = :pp WHERE Stratum_CN = :str AND Code = :code;'''
# #                    cursor.execute(sqlStr, pp = getattr(row, "ProdP"), str = currentStKIndex, code = currentSGK.SG )
# #                    if tableManager.getTag('SampleGroup', threePSGK) != getattr(row, 'ProdP'):
# #                        threePSGK = threePSGK.replace(SG = '3P-{pp}'.format(pp = getattr(row, 'ProdP')))
# #                        currentSGKIndex = tableManager.addKeyIndex('SampleGroup', threePSGK, true)
# #                        #HACK
# #                        cursor.execute('''INSERT OR FAIL INTO SampleGroup (Stratum_CN, Code, CutLeave, UOM, PrimaryProduct, SecondaryProduct, DefaultLiveDead)
# #                        SELECT Stratum_CN, :code, CutLeave, UOM, PrimaryProduct, SecondaryProduct, DefaultLiveDead  FROM SampleGroup
# #                        WHERE Stratum_CN = :str AND Code = :oldCode);''', str = currentStKIndex, code = currentSGK.SG )
# #                    else:
# #                        currentSGKIndex = tableManager("SampleGroup", threepSGK)
#                 
#                 
# #1/7/13 removed this condition because cruise processing prefers to added up count tree values 
# #        if crzMeth in ['STR', '3P', '3 P']:
# #            currentCountTreeKey = getKeyValues(row, countTreeKeyPropertys.split(), CountTreeKey)
# #            currentCountTreeKeyIndex = tableManager.getKeyIndex('CountTree', currentCountTreeKey)
# #            updateStmt = 'UPDATE CountTree set TreeCount = TreeCount + 1 WHERE CountTree_CN = {0};'.format(currentCountTreeKeyIndex)
# #            log.lg('low',updateStmt)
# #            cursor.execute(updateStmt)
# #            
#         
#         if tempTDKIndexTable.has_key(currentTDKIndex) == False:
#             chargableCode = getattr(row, "YC")
#             tempTDKIndexTable[currentTDKIndex] = [chargableCode,]
#             chargableCode = '"{0}"'.format(chargableCode) if (chargableCode != None) else "C"
#             updateStatment = 'UPDATE TreeDefaultValue SET Chargeable = {chargableCode} WHERE TreeDefaultValue_CN = {TDKIndex};'.format(chargableCode = chargableCode, TDKIndex = currentTDKIndex)
#             log.lg('low', updateStatment)
#             cursor.execute(updateStatment)
#         elif (getattr(row, "YC") in tempTDKIndexTable[currentTDKIndex]) == False:
#             chargableCode = getattr(row, "YC")
#             tempTDKIndexTable[currentTDKIndex].append(chargableCode)
#             insertStmt = 'INSERT INTO TreeDefaultValue(PrimaryProduct, Species, LiveDead, CullPrimary, HiddenPrimary, CullSecondary, HiddenSecondary, Recoverable, ContractSpecies, TreeGrade, MerchHeightLogLength, MerchHeightType, FormClass, BarkThicknessRatio, AverageZ, ReferenceHeightPercent,Chargeable)  SELECT PrimaryProduct, Species, LiveDead, CullPrimary, HiddenPrimary, CullSecondary, HiddenSecondary, Recoverable, ContractSpecies, TreeGrade, MerchHeightLogLength, MerchHeightType, FormClass, BarkThicknessRatio, AverageZ, ReferenceHeightPercent , "{chargableCode}" FROM  TreeDefaultValue WHERE TreeDefaultValue_CN = {TDKIndex};'.format(TDKIndex = currentTDKIndex, chargableCode = chargableCode)
#             log.lg('low', insertStmt)
#             currentTDKIndex = cursor.execute(insertStmt)
#             currentTDKIndex = cursor.execute('SELECT last_insert_rowid() as ID;').fetchone()[0]
#         
#         if tempSgIndexTable.has_key(currentSGKIndex) == False:
#             prodSCode = getattr(row, "ProdS")
#             tempSgIndexTable[currentSGKIndex] = prodSCode
#             prodSCode = '"{0}"'.format(prodSCode) if (prodSCode != None) else "02"
#             updateStatment = 'UPDATE SampleGroup SET SecondaryProduct = {prodS} WHERE SampleGroup_CN = {SgIndex};'.format(prodS = prodSCode, SgIndex = currentSGKIndex)
#             log.lg('low', updateStatment)
#             cursor.execute(updateStatment)
#         elif tempSgIndexTable[currentSGKIndex] != getattr(row, "ProdS"):
#             #raise Exception("same SG different Secondary Product") #TODO fix me
#             continue
#             pass
#                 
#         values = []
#         values.append(currentTDKIndex)
#         values.append(currentStTKIndex)
#         values.append(currentSGKIndex)
#         values.append(currentCUTKIndex)
#         values.append(currentPTKIndex)
#         for propName in treeDataPropertys:
#             if propName == 'CR': #CR = crown ratio
#                 value = getattr(row, propName)
#                 if value == '':
#                     value = None
#                 else:
#                     value = float(value)
#                 values.append(value)
#             else:
#                 values.append(getattr(row, propName))
#         values.append(createdBy)
#         values.append(createdDate)
#         treeData.append(TreeData(*values))
#         
#        
#         
#     tableManager.addKeyIndexs('Tree', treeKeys)
#     
#     insertData('Tree', treeDataFields.split(), treeData, cursor)
    
    
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
            log.lg('high unable to locate Tree record in log table Tree num: ' + row.Tree + ' Unit Code: ' + row.CutUnit + ' St Code: ' + row.Stratum + ' Plot Num: ' + row.Plot)
        
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
            g.Save()
        
        
    
        
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
        

    

    
    
