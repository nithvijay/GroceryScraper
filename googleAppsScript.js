function onOpen(e) {
    var ui = SpreadsheetApp.getUi();
    ui.createMenu('Dev')
        .addItem('checkNew', 'checkNew')
        .addToUi();
  }
  
  function checkNew(){
    var folder = DriveApp.getFolderById("1N1sD4-PNItoWSGAx-2ttvLhHqMdIcGsG")
    var files = folder.getFiles();
    var list = []
    while (files.hasNext()){
      main(files.next().getName());
    }
  }
    
  
  function main(csv_name){
    var ss = SpreadsheetApp.getActiveSpreadsheet()
    var sheetName = csv_name.substring(6, csv_name.length - 4);
    Logger.log(sheetName)
    var existsCheck = ss.getSheetByName(sheetName);
    if (!existsCheck){
      ss.insertSheet(sheetName);
      sheet = ss.getSheetByName(sheetName);
      var values = getCSV(sheet, csv_name);
      Logger.log(values)
      makeTitle(sheet);
      makeFormulas(sheet, values);
      setTotals(sheet, values);
      format(sheet, values);
    }
  }
  
  function getCSV(sheet, csv_name) {
    var file = DriveApp.getFilesByName(csv_name).next();
    var csvData = Utilities.parseCsv(file.getBlob().getDataAsString());
    sheet.getRange(1, 1, csvData.length, csvData[0].length).setValues(csvData);
    return csvData.length;
  }
  
  function makeTitle(sheet) {
    var range = sheet.getRange("E1:M1");
    range.setValues([["Nithin", "Bryce", "Cliff", "4th", "", "Nithin Price", "Bryce Price", "Cliff Price", "4th Price"]])
  }
  
  function makeFormulas(sheet, values) {
    var rangeTotal = sheet.getRange("I2:I" + values);
    var formulaTotal = "=SUM(R[0]C[-4]:R[0]C[-1])";
    rangeTotal.setFormulaR1C1(formulaTotal);
    var formulaPerPerson = "=R[0]C[-5]/R[0]C9*R[0]C4";
    var rangePerPerson = sheet.getRange("J2:M" + values);
    rangePerPerson.setFormulaR1C1(formulaPerPerson);
  }
  
  function setTotals(sheet, values){
    //Subtotal for all
    sheet.getRange("D" + (values + 1)).setFormula("=SUM(D2:D" + values +")")
    //Subtotal for each
    sheet.getRange("E" + (values + 1) + ":H" + (values + 1)).setFormulaR1C1("=SUM(R2C[5]:R" + (values) +"C[5])")
    //Tax
    sheet.getRange("D" + (values + 2) + ":H" + (values + 2)).setFormulaR1C1("=R[-1]C[0] * 0.026021863")
    //Totals
    sheet.getRange("D" + (values + 3) + ":H" + (values + 3)).setFormulaR1C1("=SUM(R[-2]C[0]:R[-1]C[0])")
  }
  
  function format(sheet, values) {
    sheet.getRange("A1:M1").setBorder(false, false, true, false, false, false).setFontWeight("bold");
    sheet.getRange("D" + (values + 3) + ":H" + (values + 3)).setFontWeight("bold");
    sheet.getRange("D" + (values + 1) + ":H" + (values + 1)).setBorder(true, false, false, false, false, false);
    sheet.hideColumns(9);
    sheet.autoResizeColumns(1, 15);
    sheet.setColumnWidth(1, 200);
    sheet.setColumnWidths(4, 13, 75);
    
    var range = sheet.getRange("E2:H" + values)
    var rule = SpreadsheetApp.newConditionalFormatRule()
    .whenCellNotEmpty()
    .setBackground("#b7e1cd")
    .setRanges([range])
    .build();
    var rules = sheet.getConditionalFormatRules();
    rules.push(rule);
    sheet.setConditionalFormatRules(rules);
    
  }