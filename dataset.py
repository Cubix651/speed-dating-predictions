class DataSet:
    def __init__(self, train_inputs, test_inputs, train_classes, test_classes):
        self.train_inputs = train_inputs
        self.test_inputs = test_inputs
        self.train_classes = train_classes
        self.test_classes = test_classes