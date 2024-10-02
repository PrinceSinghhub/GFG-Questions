from math import gcd


class Solution:
    def latticePointsInsideTriangle(self, p: tuple, q: tuple, r: tuple) -> int:
        def triangle_area(p1, p2, q1, q2, r1, r2):
            return abs(p1 * (q2 - r2) + q1 * (r2 - p2) + r1 * (p2 - q2)) / 2

        def boundary_points(x1, y1, x2, y2):
            return gcd(abs(x2 - x1), abs(y2 - y1)) + 1

        p1, p2 = p
        q1, q2 = q
        r1, r2 = r

        # Calculate area of the triangle
        area = triangle_area(p1, p2, q1, q2, r1, r2)

        # Calculate boundary points
        Bpq = boundary_points(p1, p2, q1, q2)
        Bqr = boundary_points(q1, q2, r1, r2)
        Brp = boundary_points(r1, r2, p1, p2)

        # Total boundary points minus the vertices counted thrice
        B = Bpq + Bqr + Brp - 3

        # Calculate interior points using Pick's Theorem
        I = area - B / 2 + 1

        return int(I)