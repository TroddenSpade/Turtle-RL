from envs.singleline import SingleLine
import gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Parallel environments
env = SingleLine()

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_singleline_tensorboard/", n_steps=512)
model.learn(total_timesteps=25000, tb_log_name="ppo_singleline")
model.save("ppo_cartpole")

del model # remove to demonstrate saving and loading

model = PPO.load("ppo_cartpole")

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
