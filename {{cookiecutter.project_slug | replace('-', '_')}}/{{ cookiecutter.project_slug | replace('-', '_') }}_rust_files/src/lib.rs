// src/lib.rs

// `` MUST BE RUN BEFORE ANY RUST INTEGRATIONS WILL WORK

/// A simple example function to compute the square of a number.
#[no_mangle]
pub extern "C" fn compute_square(x: f64) -> f64 {
    x * x
}