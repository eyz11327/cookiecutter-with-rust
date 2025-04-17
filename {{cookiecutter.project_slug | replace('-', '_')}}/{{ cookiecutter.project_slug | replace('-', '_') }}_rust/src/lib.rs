use pyo3::prelude::*;

#[pyfunction]
fn add_numbers(a: usize, b: usize) -> usize {
    a + b
}

#[pymodule]
fn _rust_functions(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    Ok(())
}
