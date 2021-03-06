import maya.cmds as cmds

class AR_OptionsWindow(object):

    @classmethod
    def showUI(cls):
        win = cls()
        win.create()
        return win

    def __init__(self):
        self.window = 'ar_optionsWindow'
        self.title = 'Options Window'
        self.size = (546,350)
        self.supportsToolAction = False
        self.actionName = 'Apply and Close'
        
    def create(self):
        if cmds.window(self.window,exists=True):
            cmds.deleteUI(self.window,window=True)

        self.window = cmds.window(
            self.window,
            title=self.title,
            widthHeight=self.size,
            menuBar=True)

        self.mainForm = cmds.formLayout(nd=100)
        self.commonMenu()
        self.commonButtons()

        self.optionsBorder = cmds.tabLayout(
            scrollable=True,
            tabsVisible=False,
            height=1,
            childResizable=True
            )
        cmds.formLayout(
            self.mainForm,e=True,
            attachForm =(
                [self.optionsBorder,'top',0],
                [self.optionsBorder,'left',2],
                [self.optionsBorder,'right',2]
                ),
            attachControl=(
                [self.optionsBorder,'bottom',5,self.applyBtn]
                )
            )
        self.optionsForm = cmds.formLayout(nd=100)
        
        # cmds.formLayout(
        #     self.mainForm,e=True,
        #     attachForm =(
        #         [self.optionsForm,'left',3],
        #         [self.optionsForm,'right',3]
        #         )
        #     )
        self.displayOptions()

        cmds.showWindow()        

    def commonMenu(self):
        self.editMenu = cmds.menu(label='Edit')
        self.editMenuSave = cmds.menuItem(
            label = 'Save Settings'
            )
        self.editMenuReset = cmds.menuItem(
            label = 'Reset Settings'
            )
        self.editMenuDiv = cmds.menuItem(d=True)
        self.editMenuRadio = cmds.radioMenuItemCollection()
        self.editMenuTool = cmds.menuItem(
            label = 'As Tool',
            radioButton = True,
            enable = self.supportsToolAction
            )
        self.editMenuAction = cmds.menuItem(
            label='As Action',
            radioButton=True,
            enable=self.supportsToolAction
            )
        self.helpMenu = cmds.menu(label='Help')
        self.helpMenuItem = cmds.menuItem(
            label='Help on %s'%self.title,
            command=self.helpMenuCmd
            )

    def commonButtons(self):
        self.commonBtnSize = ((self.size[0]-18)/3,26)

        self.actionBtn = cmds.button(
                label=self.actionName,
                height=self.commonBtnSize[1],
                command=self.actionBtnCmd
            )

        self.applyBtn = cmds.button(
                label='Apply',
                height=self.commonBtnSize[1],
                command=self.applyBtnCmd
            )
        
        self.closeBtn = cmds.button(
            label='Close',
            height=self.commonBtnSize[1],
            command=self.closeBtnCmd
            )

        cmds.formLayout(
            self.mainForm,e=True,
            #specifies edges on controls
            attachForm=(
                [self.actionBtn,'left',5],
                [self.actionBtn,'bottom',5],
                [self.applyBtn,'bottom',5],
                [self.closeBtn,'bottom',5],
                [self.closeBtn,'right',5]
                ),
            attachPosition=(
                [self.actionBtn,'right',1,33],
                [self.closeBtn,'left',0,67]
                ),
            attachControl=(
                [self.applyBtn,'left',4,self.actionBtn],
                [self.applyBtn,'right',4,self.closeBtn]
                ),
            attachNone = (
                [self.actionBtn,'top'],
                [self.applyBtn,'top'],
                [self.closeBtn,'top']
                )
            )

    def helpMenuCmd(self,*args):
        cmds.launch(web='http://maya-python.com')

    def editMenuSaveCmd(self,*args):
        pass

    def editMenuResetCmd(self,*args):
        pass

    def editMenuToolCmd(self,*args):
        pass

    def editMenuActionCmd(self,*args):
        pass

    def actionBtnCmd(self,*args):
        self.applyBtnCmd()
        self.closeBtnCmd()

    def applyBtnCmd(self,*args):
        pass

    def closeBtnCmd(self,*args):
        cmds.deleteUI(self.window,window=True)

    def displayOptions(self):
        pass









    
        
        