# encoding=utf8
# pylint: disable=mixed-indentation, redefined-builtin
from math import pow
from unittest import TestCase
from numpy import asarray
from NiaPy.benchmarks.utility import Utility


class TestBenchmarkFunctions(TestCase):

	# pylint: disable=too-many-instance-attributes,too-many-public-methods
	def setUp(self):
		self.D = 5
		self.array = asarray([0, 0, 0, 0, 0])
		self.array2 = asarray([1, 1, 1, 1, 1])
		self.array3 = asarray([420.968746, 420.968746, 420.968746, 420.968746, 420.968746])
		self.array4 = asarray([-2.903534, -2.903534])
		self.array5 = asarray([-0.5, -0.5, -0.5, -0.5, -0.5])
		self.array6 = asarray([-1, -1, -1, -1, -1])
		self.array7 = asarray([2, 2, 2, 2, 2])
		self.array8 = asarray([7.9170526982459462172, 7.9170526982459462172, 7.9170526982459462172, 7.9170526982459462172, 7.9170526982459462172])
		self.array9 = asarray([-5.12, -5.12, -5.12, -5.12, -5.12])
		self.array10 = asarray([1, 2, 3, 4, 5])

	def assertBounds(self, bench, l, u):
		b = Utility().get_benchmark(bench)
		self.assertEqual(b.Lower, l)
		self.assertEqual(b.Upper, u)
		return b.function()

	def test_rastrigin(self):
		rastrigin = Utility().get_benchmark('rastrigin')
		fun = rastrigin.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_rosenbrock(self):
		rosenbrock = Utility().get_benchmark('rosenbrock')
		fun = rosenbrock.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array2), 0.0)

	def test_griewank(self):
		griewank = Utility().get_benchmark('griewank')
		fun = griewank.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_sphere(self):
		sphere = Utility().get_benchmark('sphere')
		fun = sphere.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_ackley(self):
		ackley = Utility().get_benchmark('ackley')
		fun = ackley.function()
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array), 0.0, places=10)

	def test_schwefel(self):
		schwefel = Utility().get_benchmark('schwefel')
		fun = schwefel.function()
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array3), 0.0, places=3)

	def test_schwefel221(self):
		schwefel221 = Utility().get_benchmark('schwefel221')
		fun = schwefel221.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_schwefel222(self):
		schwefel222 = Utility().get_benchmark('schwefel222')
		fun = schwefel222.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_whitley(self):
		whitley = Utility().get_benchmark('whitley')
		fun = whitley.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array2), 0.0)

	def test_styblinskiTang(self):
		styblinskiTang = Utility().get_benchmark('styblinskiTang')
		fun = styblinskiTang.function()
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(2, self.array4), -78.332, places=3)

	def test_sumSquares(self):
		sumSquares = Utility().get_benchmark('sumSquares')
		fun = sumSquares.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_stepint(self):
		stepint = Utility().get_benchmark('stepint')
		fun = stepint.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array9), 25.0 - 6 * self.D)

	def test_step(self):
		step = Utility().get_benchmark('step')
		fun = step.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_step2(self):
		step2 = Utility().get_benchmark('step2')
		fun = step2.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array5), 0.0)

	def test_step3(self):
		step3 = Utility().get_benchmark('step3')
		fun = step3.function()
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_schumerSteiglitz(self):
		fun = self.assertBounds('schumerSteiglitz', -100, 100)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_salomon(self):
		fun = self.assertBounds('salomon', -100.0, 100.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_quintic(self):
		fun = self.assertBounds('quintic', -10.0, 10.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array6), 0.0)

	def test_quintic2(self):
		fun = self.assertBounds('quintic', -10.0, 10.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array7), 0.0)

	def test_pinter(self):
		fun = self.assertBounds('pinter', -10.0, 10.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_alpine1(self):
		fun = self.assertBounds('alpine1', -10.0, 10.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_alpine2(self):
		fun = self.assertBounds('alpine2', 0.0, 10.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array8), pow(2.8081311800070053291, self.D))

	def test_chungReynolds(self):
		fun = self.assertBounds('chungReynolds', -100, 100)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_csendes(self):
		fun = self.assertBounds('csendes', -1.0, 1.0)
		self.assertTrue(callable(fun))
		self.assertEqual(fun(self.D, self.array), 0.0)

	def test_bentcigar(self):
		fun = self.assertBounds('bentcigar', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 54000001.0, delta=1e-4)

	def test_discus(self):
		fun = self.assertBounds('discus', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 1000054.0, delta=1e-4)

	def test_elliptic(self):
		fun = self.assertBounds('elliptic', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 5129555.351959938, delta=2e6)

	def test_expanded_griewank_plus_rosnbrock(self):
		fun = self.assertBounds('expandedgriewankplusrosenbrock', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 854123.5271421941, delta=1e2)

	def test_expanded_scaffer(self):
		fun = self.assertBounds('expandedscaffer', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 2.616740208857464, delta=1e-4)

	def test_hgbat(self):
		fun = self.assertBounds('hgbat', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 61.91502622129181, delta=60)

	def test_katsuura(self):
		fun = self.assertBounds('katsuura', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 3837.4739882594373, delta=4000)

	def test_modifiedscwefel(self):
		fun = self.assertBounds('modifiedscwefel', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 6.9448853328785844, delta=350)

	def test_weierstrass(self):
		fun = self.assertBounds('weierstrass', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 0.0, delta=1e-4)

	def test_happyCat(self):
		fun = self.assertBounds('happyCat', -100, 100)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 15.1821333, delta=1e-4)

	def test_qing(self):
		fun = self.assertBounds('qing', -500, 500)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 669.0, delta=1e-4)

	def test_ridge(self):
		fun = self.assertBounds('ridge', -64, 64)
		self.assertTrue(callable(fun))
		self.assertAlmostEqual(fun(self.D, self.array10), 371.0, delta=1e-4)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
