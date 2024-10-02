class Solution:

    def safePos(self, n, k):
        # Your code here

        a = [i for i in range(1, n + 1)]  # array of number of of persons sitting in circle

        gun = 0  # pos of guy with the gun

        # print(a)

        # print(((gun+k)-1)%len(a))

        def survive(gun, a):
            if len(a) == 1:
                return a[0]  # only survivor at the end

            kill = ((gun + k) - 1) % len(a)  # pos of guy to be killed

            """

            if 0 pos guy has gun and k is 2 then count will be 2 at 1 pos guy and he will be killed

            """

            a.pop(kill)  # guy is killed

            gun = kill  # passing the gun to the guy next to dead

            return survive(gun, a)  # recursive call

        return survive(gun, a)