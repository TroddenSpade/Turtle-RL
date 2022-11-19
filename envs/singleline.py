import gym
import numpy as np
import skimage.draw as draw
import matplotlib.pyplot as plt


class SingleLine(gym.Env):
    def __init__(self, shape=(800, 800)):
        super(SingleLine, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=shape+(3,), dtype=np.uint8)
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(1,), dtype=np.float32)
        self.shape = shape
        self.points = []
        with open('coords.txt') as f:
            lines = f.readlines()
            for line in lines:
                arr = line.split(" ")
                self.points.append([int(arr[1]), int(arr[2])])
        self.points = np.array(self.points)



    def create_board(self, ps):
        board = np.zeros(self.observation_space.shape, dtype=np.uint8)
        indexes = np.ones(self.shape, dtype=int) * -1

        for i, p in enumerate(ps):
            rr, cc = draw.disk(p, 5, shape=self.shape)
            board[rr, cc] = 128
            indexes[rr, cc] = i

        return board, indexes


    def delete_points(self, ps):
        for p in ps:
            rr, cc = draw.disk(p, 5, shape=self.shape)
            self.board[rr, cc] = 0


    def step(self, action):
        self.steps += 1
        done = False if self.steps < 1000 else True

        action = np.clip(action, -1, 1)[0]
        self.angle += action * np.pi/2
        end = (self.start + self.l * np.array([np.cos(self.angle), np.sin(self.angle)])).astype(int)

        if not (0 <= end[0] < self.shape[0] and 0 <= end[1] < self.shape[1]):
            return self.state, -5, done, {}

        rr, cc, val = draw.line_aa(self.start[0], self.start[1], end[0], end[1])
        self.board[rr, cc, 0] = val * 255
        self.start = end

        idxs = np.unique(self.indexes[rr, cc])
        idxs = idxs[idxs >= 0]

        self.delete_points(self.points[idxs])

        r = idxs.size
        if r == 0:
            reward = -1
        else:
            reward = r

        self.state = self.board.copy()
        rr, cc = draw.disk(end, 5)
        self.state[rr, cc, 0] = 255
        return self.state, reward, done, {}


    def reset(self):
        self.board, self.indexes = self.create_board(self.points)

        self.state = None
        self.l = 10
        self.start = self.points[0]
        self.steps = 0

        self.angle = np.random.uniform(-np.pi, np.pi)
        end = (self.start + self.l * np.array([np.cos(self.angle), np.sin(self.angle)])).astype(int)
        rr, cc, val = draw.line_aa(self.start[0], self.start[1], end[0], end[1])
        self.board[rr, cc, 0] = val * 255
        self.start = end

        idxs = np.unique(self.indexes[rr, cc])[1:]
        self.delete_points(self.points[idxs])

        self.state = self.board.copy()
        rr, cc = draw.disk(end, 5)
        self.state[rr, cc, 0] = 255
        return self.state


if __name__ == '__main__':
    env = SingleLine()
    for i in range(100):
        env.reset()
        for j in range(10):
            state, reward, done, _ = env.step(np.random.uniform(-1, 1, size=(1,)))
            print(reward)
            plt.imshow(state)
            plt.show()
            plt.pause(0.01)