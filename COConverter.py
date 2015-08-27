'''
Created on Jul 1, 2011
@author: benjaminjcampbell
'''
import os #for path functions
import clr 
import metakit
import Logger #for message logging
import sys

clr.AddReference('CruiseDAL')
from CruiseDAL import DAL


CURRENT_CRZ_STRUCTURE_VERSION = '2010.03.18'

FAIL_MESSAGE = "FAIL"
PROGRESS_STEP_INDICATOR = "."
log = Logger.Logger()


#createSQLFilePath = os.path.dirname(__file__) + '\\CruiseCreate.sql'
#createSQLFilePath = r'.\CruiseCreate.sql'

def Run(inputPath, outputPath):
    success = False
    conn = None
    cursor = None
    isOverwriting = False 
    existingPath = None
    
    #check for create curise file
#     if not os.path.exists(createSQLFilePath):
#         log.lg("high", "ERROR resource file CruiseCreate.sql not found")
#         
#         
#         success = False
#         return success
    
    #check output file extention
    if not str.lower(outputPath[-7:]) == '.cruise':
        log.lg("high", "ERROR outputFile has bad extention")
        success = False
        return success
        
    #check if overwriting existing filename
#     if(os.path.exists(outputPath)):
#         log.lg('norm', 'existing file found: overwriting')
#         isOverwriting = True
#         existingPath = outputPath
#         outputPath = outputPath + '.new'
        
    #check input file and extention
    if not str.lower(inputPath[-4:]) == '.crz':
        log.lg("high", "ERROR file to convert has wrong extention")
        success = False
        return success
    
    if not os.path.exists(inputPath):
        log.lg("high", "ERROR Couldn't find file to convert")
        success = False
        return success
    
    #load input file 
    mk = metakit.storage(inputPath,0)
    #check crz file version of the input file
    if not isCRZCurrent(mk):
        log.lg('high', 'ERROR CRZ file not current version')
        success = False
        return success
    
    #try:
        #create database connecting and cursor
    print(outputPath)
    dal = DAL(outputPath, True)
    dal.Create()
#         cursor = conn.cursor()
    #cereate database
#         import codecs 
#         createSQLFile = codecs.open(createSQLFilePath, 'rb','utf-8-sig')# http://stackoverflow.com/questions/2359832/dealing-with-utf-8-numbers-in-python
#         #createSQLFile = open(createSQLFilePath, 'rb')
#         createDBFile(conn, cursor, createSQLFile)
    incrementProgress()
    
    #process CRZ file and fill db file
    log.lg("norm", 'processing metakit file')
    processCRZFile(mk, dal)
    
    #clean up overwritten file of overwriting
#         if isOverwriting:
#             os.remove(existingPath)
#             os.rename(outputPath, existingPath)
    dal.Path = outputPath
    success = True
         
#     except Exception as er: 
#         log.lg('high', 'PROGRAM ERROR program ended in error, exception args: ' + repr(er.args))
#         log.lg('high', 'PROGRAM ERROR program ended in error, exception message: ' + repr(er.message))
#         #log.lg('high', sys.exc_info())
#         #os.remove(outputPath)#filling database failed remove it
#         success = False
# 
#     finally:
#         pass
#         if not cursor is None: 
#             cursor.close()
#         if not conn is None:
#             conn.close()
        

        
    return success

def dumpLog(logPath):
    #log.display(reportingLevel)
    log.dump(reportingLevel, logPath)
        
def isCRZCurrent(metaKitFile):
    globalView = metaKitFile.view('GlobalConfigurationTable')
    for row in globalView:
        if getattr(row,'Key') == 'StructureVersion' and getattr(row,'Block') == 'General':
            if getattr(row,'Value') == CURRENT_CRZ_STRUCTURE_VERSION:
                return True
            else:
                return False
    
    return False   


def writeMessageLog(cursor):
    cursor.execute("insert into messagelog (program, message, date, time) values ('crz converter utility', 'crz file converted', current_date, current_time)")
    

# def createDBFile(conn, cursor, createSQLFile):
#     try:
#         text = ' '.join(createSQLFile.readlines())
#         cursor.executescript(text)
#             
#     except Exception as er:
#         log.lg('high','PROGRAM ERROR fail while defining db schema')
#         
#         raise er

def incrementProgress():
    print(PROGRESS_STEP_INDICATOR)                                
  
def processCRZFile(mk, dal):

    
    import ViewReaders

    #for all the views in the metakit file
    #we will grab the view and pass it to 
    #its corisponding viewReader.
    #the view reader will read the data and 
    #insert it into the database file
    
    vw = mk.view('CruiseTable')
    ViewReaders.readCruiseTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('CuttingUnitTable')
    ViewReaders.readCuttingUnitsTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('StratumTable')
    ViewReaders.readStratumTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('SubPopulationTable')
    ViewReaders.readSubPopTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('CountTable')
    ViewReaders.readCountTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('PlotTable')
    ViewReaders.readPlotTable(vw, dal)
    incrementProgress() 
    
    vw = mk.view('TreeTable')
    ViewReaders.readTreeTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('LogTable')
    ViewReaders.readLogTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('VolumeEquationTable')
    ViewReaders.readVoumeEquTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('GlobalConfigurationTable')
    ViewReaders.readGlobalConfigTable(vw, dal)
    incrementProgress()
    
    vw = mk.view('MessageLog')
    ViewReaders.readMessageLogTable(vw, dal)
    incrementProgress() 
    
    #vw = mk.view('WeightEquationTable')
    #ViewReaders.readWeightEquationTable(vw, conn, cursor)
    #incrementProgress()
    
#     writeMessageLog(cursor)
    
    print("...Done...")
     




if __name__ == '__main__':
    
    import getopt 
    
    success = True
    reportingLevel = 'verbose'
    #verbose = false;
    waitOnFinish = False;
    forceDumpFile = False
    
    optlist, args = getopt.getopt(sys.argv[1:], 'dvw')
    log.lg('low', 'optlist: ' + str(optlist))
    log.lg('low', 'args: ' + str(args))
    for item in optlist:
        if item[0] == '-v':
            verbose = True;
            pass
        if item[0] == '-w':
            waitOnFinish = True
            pass
        if item[0] == '-d':
            forceDumpFile = True
            pass
        
        
    
    outputPath = None
    sourceFileName = None
    sourcePath = None
    
    if len(args) >= 1 :
        sourcePath = args[0]
        sourceFileName = os.path.split(sourcePath)[1]
        log.lg('low','sourcePath: ' + sourcePath)
        log.lg('low','sourceFileName: ' + sourceFileName)
        
        if len(args) >= 2:
            outputPath = args[1]
        else:
            outFileName = os.path.splitext(sourceFileName)[0] + '.cruise'
            outputPath = os.path.dirname(sourcePath) + '\\' + outFileName
           
        log.lg('low','outputPath: ' + outputPath) 
        logPath = os.path.dirname(sourcePath) + "\\COConverterLog.txt"
        
        try:
            if not Run(sourcePath, outputPath):
                success = False
        except Exception as e:
            import traceback
            log.lg('high', str(traceback.format_exc()))
            success = False
            if(waitOnFinish):
                raw_input('press any key to exit:_')
                pass
            sys.exit(1)
            pass
        
        if not success:
            print(FAIL_MESSAGE)
            dumpLog(logPath)    
        else:
            if forceDumpFile:
                dumpLog(logPath)
                
    else:
        print('Error incorrect arguments ( [-d] [-w] [-v] sourcePath [outputPath] )')
        
    if(waitOnFinish):
        raw_input('press any key to exit:_')
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)

    
    
#     elif( len(args) == 3):
#         if not Run(sys.argv[1], sys.argv[2]):
#             print(FAIL_MESSAGE)
#             
#             
#             logPath = os.path.dirname(sys.argv[1]) + "\\COConverterLog.txt"
#             dumpLog(logPath)
#             sys.exit(1)
#         else:
#             logPath = os.path.dirname(sys.argv[1]) + "\\COConverterLog.txt"
#             dumpLog(logPath)
            
                   

                            
        
    
    