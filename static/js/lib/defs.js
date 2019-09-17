Blockly.Blocks['actions_fill'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("fill")
        .appendField(new Blockly.FieldVariable(), "NAME");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(180);
 this.setTooltip("Fill");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['actions_click'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("click")
        .appendField(new Blockly.FieldTextInput("default"), "NAME");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Click");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['actions_wait'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("wait")
        .appendField(new Blockly.FieldNumber(0, 0), "NAME")
        .appendField("ms");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(90);
 this.setTooltip("Wait");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['group_procedure'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("procedure")
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(60);
 this.setTooltip("Procedure");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['group_sub_procedure'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("sub procedure")
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(80);
 this.setTooltip("Sub Procedure");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['actions_start'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Start");
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("Start");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['reports_simple'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("generate report");
    this.setPreviousStatement(true, null);
    this.setColour(270);
 this.setTooltip("Generate an Execution Summary");
 this.setHelpUrl("");
  }
};