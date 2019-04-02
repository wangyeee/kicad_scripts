import pcbnew

class SmallTextSize(pcbnew.ActionPlugin):

    def defaults(self):
        self.name = 'SmallTextSize'
        self.category = 'Modify PCB'
        self.description = 'Make texts smaller on PCB'

    def Run(self):
        board = pcbnew.GetBoard()
        newThickness = 100000
        newWidth = 400000
        newHeight = 400000
        for module in board.GetModules():
            val = module.Value()
            val.SetThickness(newThickness)
            val.SetTextWidth(newWidth)
            val.SetTextHeight(newHeight)
            ref = module.Reference()
            ref.SetThickness(newThickness)
            ref.SetTextWidth(newWidth)
            ref.SetTextHeight(newHeight)
            for otr in module.GraphicalItemsList():
                if isinstance(otr, pcbnew.TEXTE_MODULE):
                    otr.SetVisible(False)
        pcbnew.Refresh()

SmallTextSize().register()
