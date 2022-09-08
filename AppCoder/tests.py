from django.test import TestCase
from django.urls import reverse

from AppCoder.models import Curso


class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(nombre="Python1", camada=1)
        Curso.objects.create(nombre="Python2", camada=2)

    def test_animals_can_speak(self):
        p1 = Curso.objects.get(camada=1)
        p2 = Curso.objects.get(camada=2)
        self.assertEqual(p1.nombre, 'Python1')
        self.assertEqual(p2.nombre, 'Python2')


class ViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('AppCoderInicio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay nada para mostrar")

    def test_past_question(self):
        curso = Curso.objects.create(nombre="Python1", camada=1)
        response = self.client.get(reverse('AppCoderCurso'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f"el curso es: { curso.nombre } camada { curso.camada }"
        )
