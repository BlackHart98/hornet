import agent
import environment
class adder(agent.agent):
    def policy(self,state):
        action=state
        for i in range(len(action)):
            action[i]+=1
        return action

class diminisher(agent.agent):
    def policy(self,state):
        action=state
        for i in range(len(action)):
            action[i]-=1
        return action
        
class envt(environment.environment):
    def do(self,action):
        self.state=action

if __name__=='__main__':
    env=envt([0,0])
    agnt=adder()
    agnt_1=diminisher()
    i=10
    while i>0:
        act=agnt.policy(env.state)
        env.do(act)
        act=agnt_1.policy(env.state)
        env.do(act)
        print(env.state)
        i-=1
    
    