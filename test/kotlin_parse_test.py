from parser_ts import get_kotlin_class

kotlin_code = """
/**
 * Simple Test Class
 */
class Car {
    // class data
    companion object {
        @JvmField
        private var nrInstances: Int = 0
    } 

    public var brand = "none"
    public var model: String
    private var kilometersDriven: Int = 0

    init {
        nrInstances++
    }

    // class function to drive the car
    fun drive(distance: Int): Unit  {
        kilometersDriven += distance
    }

    // @return the number of instances of Car
    fun getNrOfCars(): Int {
        return protectedGetNrOfCars()
    }

    protected fun protectedGetNrOfCars(): Int {
        return privateGetNrOfCars()
    }

    private fun privateGetNrOfCars(): Int {
        return nrInstances
    }
}
"""


def test_kotlin_parse() -> None:
    kotlin_class = get_kotlin_class(kotlin_code, "Car")

    methods = kotlin_class.get_methods()

    assert len(methods) == 4
    assert (
        methods[0]
        == """fun drive(distance: Int): Unit  {
        kilometersDriven += distance
    }"""
    )
    assert (
        methods[1]
        == """fun getNrOfCars(): Int {
        return protectedGetNrOfCars()
    }"""
    )
    assert (
        methods[2]
        == """protected fun protectedGetNrOfCars(): Int {
        return privateGetNrOfCars()
    }"""
    )
    assert (
        methods[3]
        == """private fun privateGetNrOfCars(): Int {
        return nrInstances
    }"""
    )
