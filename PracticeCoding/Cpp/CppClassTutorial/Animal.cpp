#include <iostream>

using namespace std;

#include <string.h>

class Animal {

	//Overload Constructor when nothing is passed.
	Animal();
	Animal()

	public:
		int getHeight() {
			return height;
		}
		int getWeight() {
			return weight;
		}
		void setWeight(int inputWeight) {
			weight = inputWeight;
		}
		void setHeight(int inputHeight) {
			height = inputHeight;
		}


		
	private:
		string name;
		int height;
		int weight;



};

int main() {

}