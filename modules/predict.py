import torch

class Predict:
    def __init__(self,model,data,label):
        self.model = model
        self.data = data
        self.label = label

    def predictOne(self):
        inputs = inputs.to(self.data)
        outputs = self.model(inputs)
        _, preds = torch.max(outputs, 1)
        res = self.label[preds]


        return res

    def predictMul(self):
        res = []
        for d in self.data:
            inputs = inputs.to(d)
            outputs = self.model(inputs)
            _, preds = torch.max(outputs, 1)
            res.append(self.label[preds])

        return res