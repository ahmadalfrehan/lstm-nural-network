from experta import *
class ComputeFactorial(KnowledgeEngine):
    @Rule(Fact(x=MATCH.value))
    def factorial(self,value):
        self.declare(
            Fact(x=value,y=1))
         
cf = ComputeFactorial()
cf.reset()
cf.declare(Fact(x=5))
cf.run()
cf.facts

