import torch

class LoadModel:
    def __init__(self,model_option):
        self.model_option = model_option

    def getPath(self):
        path = ''
        if self.model_option == 'Model1':
            path = './models/model_conv_1.pt'

        elif self.model_option == 'Model2':
            path = './models/model_conv_2.pt' 

        elif self.model_option == 'Model3':
            path = './models/model_ghost.pt'

        elif self.model_option == 'Model4':
            path = './models/model_ghost.pt'

        elif self.model_option == 'Model5':
            path = './models/model_ghost.pt'

        return path

    def load(self):
        path = self.getPath()
        model = torch.load(path)
        model.eval()
