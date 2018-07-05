//Guntas Singh
//Thapar University Patiala
#include <iostream>
using namespace std;
void Multiply_Matrix(int matrix[][100],int Kernel[][100],int sizeofmatrix,int sizeofKernel,int i,int j,int multiplied[][100])
{
	int multiply=0;
	int ki=0,kj=0;
	if(j+sizeofKernel==sizeofmatrix+1)
	{
		Multiply_Matrix(matrix,Kernel,sizeofmatrix,sizeofKernel,i+1,0,multiplied);
	}
	if(j+sizeofKernel==sizeofmatrix+1 && i+sizeofKernel==sizeofmatrix+1)
	{
	return;
		}
	if(j+sizeofKernel>sizeofmatrix+1)
	{
		return;
	}
	if(i+sizeofKernel>sizeofmatrix+1)
	{
		return;
	}
	for(int row=i;row<sizeofKernel+i;row++)
		{	kj=0;
			for(int col=j;col<sizeofKernel+j;col++)
			{	
				multiply += matrix[row][col]*Kernel[ki][kj];
				kj++;
			}
			ki++;
		}	
		cout<<multiply<<endl;
		multiplied[i][j]=multiply;
		Multiply_Matrix(matrix,Kernel,sizeofmatrix,sizeofKernel,i,j+1,multiplied);
}

void InputMatrix(int matrix[100][100],int sizeofmatrix)
{
	for(int rows=0;rows<sizeofmatrix;rows++)
	{
		for(int cols=0;cols<sizeofmatrix;cols++)
		{
			cin>>matrix[rows][cols];
		}
	}
}
void OutputMatrix(int matrix[100][100],int sizeofmatrix)
{
	for(int rows=0;rows<sizeofmatrix;rows++)
	{
		for(int cols=0;cols<sizeofmatrix;cols++)
		{
			cout<<matrix[rows][cols]<<" ";
		}
		cout<<endl;
	}
}
int main()
{
	int sizeofmatrix,sizeofKernel;
	cin>>sizeofmatrix;
	cin>>sizeofKernel;
	int matrix[100][100];
	int Kernel[100][100];
	int multiplied[100][100];
	for(int rows=0;rows<sizeofmatrix-1;rows++)
	{
		for(int cols=0;cols<sizeofmatrix-1;cols++)
		{
			multiplied[rows][cols]=0;
		}
	}
	InputMatrix(matrix,sizeofmatrix);
	InputMatrix(Kernel,sizeofKernel);
	Multiply_Matrix(matrix,Kernel,sizeofmatrix,sizeofKernel,0,0,multiplied);
	OutputMatrix(multiplied,sizeofmatrix-1);
}