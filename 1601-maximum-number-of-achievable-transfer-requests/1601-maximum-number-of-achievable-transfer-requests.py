class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0

        def dfs(index, balance, count, n_requests):
            nonlocal max_requests

            if index == n_requests:
                for b in balance:
                    if b != 0:
                        return

                max_requests = max(max_requests, count)
                return

            fromi, toi = requests[index]

            balance[fromi] -= 1
            balance[toi] += 1
            dfs(index + 1, balance, count + 1, n_requests)
            balance[fromi] += 1
            balance[toi] -= 1
            dfs(index + 1, balance, count, n_requests)

        balance = [0] * n
        dfs(0, balance, 0, len(requests))

        return max_requests
        