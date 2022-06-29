using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace IgoryanFloat
{
    public partial class Form1 : Form
    {
        
        int n;
        int k;
        int rezult;

        public Form1()
        {
            InitializeComponent();
        }

        public int Factorial(int n)
        {
            if (n <= 0)
            {
                MessageBox.Show("Факториал меньше или равен нулю");
                return 0;
            }
            else
            {
                int factorial = 1;
                for (int i = 1; i <= n; i++)
                    factorial = factorial * i;
                return factorial;
            }

        }
        private void button1_Click_1(object sender, EventArgs e)
        {
            try
            {
                n = Convert.ToInt32(textBox1.Text);
                rezult = Factorial(n);

                label3.Text = "Получаем ответ: P(n) = n! = " + rezult;
            }
            catch
            {
                MessageBox.Show("Вы ввели данные некорректно, пожалуйста, введите правильно");
            }
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            try
            {
                n = Convert.ToInt32(textBox1.Text);
                k = Convert.ToInt32(textBox2.Text);
                if (k >= n) MessageBox.Show("Делить на ноль нельзя.Значение k должно быть меньше значения n");
                else
                {
                    rezult = Factorial(n) / Factorial(n - k);
                    label3.Text = "Получаем ответ:  n!/(n-k)! = " + rezult;
                }
            }
            catch
            {
                MessageBox.Show("Вы ввели данные некорректно, пожалуйста, введите правильно");
            }
        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            try
            {
                n = Convert.ToInt32(textBox1.Text);
                k = Convert.ToInt32(textBox2.Text);
                if (k >= n) MessageBox.Show("Делить на ноль нельзя.Значение k должно быть меньше значения n");
                else
                {
                    rezult = Factorial(n + k - 1) / (Factorial(k) * Factorial(n - 1));
                    label3.Text = "Получаем ответ: С (k n) = С (k n+k-1) = (n+k-1)!/(k!(n-1)!) = " + rezult;
                }
            }
            catch
            {
                MessageBox.Show("Вы ввели данные некорректно, пожалуйста, введите правильно");
            }
        }

        private void button5_Click_1(object sender, EventArgs e)
        {
            try
            {
                n = Convert.ToInt32(textBox1.Text);
                k = Convert.ToInt32(textBox2.Text);
                if (k >= n) MessageBox.Show("Делить на ноль нельзя.Значение k должно быть меньше значения n");
                else
                {
                    rezult = Factorial(n) / Factorial(n - k);
                    label3.Text = "Получаем ответ: А (k n) = n!/(n-k)! = " + rezult;
                }
            }
            catch
            {
                MessageBox.Show("Вы ввели данные некорректно, пожалуйста, введите правильно");
            }
        }

        private void button6_Click_1(object sender, EventArgs e)
        {
            try
            {
                double n = Convert.ToDouble(textBox1.Text);
                double k = Convert.ToDouble(textBox2.Text);
                double rezult = Math.Pow(n, k);
                label3.Text = "Получает ответ: A (k n) = n^k = " + rezult;
            }
            catch
            {
                MessageBox.Show("Вы ввели данные некорректно, пожалуйста, введите правильно");
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            try
            {
                n = Convert.ToInt32(textBox1.Text);
                k = Convert.ToInt32(textBox2.Text);
                if (k >= n) MessageBox.Show("Делить на ноль нельзя.Значение k должно быть меньше значения n");
                else
                {
                    rezult = Factorial(n) / (Factorial(k) * Factorial(n - k));
                    label3.Text = "Получаем ответ: С (k n) = n!/((n-k)!k!) = " + rezult;
                }
            }
            catch
            {
                MessageBox.Show("Вы ввели данные некорректно, пожалуйста, введите правильно");
            }
        }
    }
   

       
    
}
