"""make imports"""
#developed by kinsley kajiva 
#this was made in python 3.6
# this was downloaded from https://github.com/kinsleykajiva/Neural-Network--simple-Perceptron--In-python

#just Compile 
class NetNuron(object):
	__countingSelf=0
	__eporchCounts=0
	
	def __int__(self):
		print("Net.......Running.....")
		
	def whatYouCanDo(self):
		print("Hey thanx for using this.......\n",
			"You can always change the weights and other inputs....\n\n\n\n\n"
			)
		pass

	def threshHoldFunction(self,inputs,weights):
		sumProduct=0.0
		for i in range(0,len(weights)):
			sumProduct+=inputs[i]*weights[i]			
		return sumProduct

	def PerceptronWeightUpdate(self,W_old,learningRate,desired,networkOuput,inputValue):
		self.__countingSelf=self.__countingSelf+1
		print("\t\tUpdating weight ",self.__countingSelf)
		newW=W_old + learningRate*(desired - networkOuput) * inputValue
		print("\t\t\t",newW,"=",W_old,"+",learningRate,"*(",desired,"-",networkOuput,")*",inputValue)	
		
		return newW
	
	def runPerceptron(self,input_X,weight_X,threshold,DecisionThreshHold=0):
		returnHold=self.threshHoldFunction(input_X,weight_X)
		if returnHold>=threshold:
			print("Done Network Results is Desirable = ",returnHold)			
		else:
			print("Updating weights output is :",returnHold)
			for i in range(0,len(weight_X)):
				"""create a new weight"""
				NewWeight=self.PerceptronWeightUpdate(weight_X[i],learningRate_Alpha,desiredOutput,DecisionThreshHold,input_X[i])
				"""now replace the old weight in the list at position i with new wieght"""
				weight_X[i]=NewWeight
				networkOuput_=self.threshHoldFunction(input_X,weight_X)
			self.__eporchCounts=self.__eporchCounts+1
			if networkOuput_>=threshold:
				print("Now exiting conditions has been met : ",networkOuput_," in ",self.__eporchCounts,"count of eporches")	
				print("\n")	
			else:
				print("******Recurssing again*********")
				self.runPerceptron(input_X,weight_X,threshold,DecisionThreshHold)


"""provide inputs"""
input_X=	[20,-6,.5,-10]
weight_X=	[10,10,5,20]
threshold=20
learningRate_Alpha=1
desiredOutput=1
mNetNuron=NetNuron()

DecisionThreshHold=0
mNetNuron.whatYouCanDo()
mNetNuron.runPerceptron(input_X,weight_X,threshold)
















