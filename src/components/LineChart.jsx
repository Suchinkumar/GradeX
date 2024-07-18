import React, { useEffect, useRef } from 'react';
import { Chart } from 'frappe-charts';


const LineChart = ({ data, title, which }) => {
    const chartRef = useRef(null);
    let check = 0;

    const allMarks = (new Array(Number.parseInt(data.totalMarks))).fill(0).map((_, i) => i)
    allMarks.push(Number.parseInt(data.totalMarks))

    const allTestCases = (new Array(Number.parseInt(data.totalTestCases))).fill(0).map((_, i) => i)
    allTestCases.push(Number.parseInt(data.totalTestCases))

    if (which == "testcase") {
        check = 1;
    }

    useEffect(() => {
        let marks = {};
        if (which == "marks") {
            marks = data.students.reduce((acc, student) => {
                const marks = parseInt(student.totalMarks);
                if (!acc[marks]) {
                    acc[marks] = 0;
                }
                acc[marks]++;
                return acc;
            }, {})
        } else {
            marks = data.students.reduce((acc, student) => {
                const marks = parseInt(student.testcasesPassed);
                if (!acc[marks]) {
                    acc[marks] = 0;
                }
                acc[marks]++;
                return acc;
            }, {})
        }

        const chart = new Chart(chartRef.current, {
            title: title,
            data: {
                labels: check ? allTestCases : allMarks,
                datasets: [
                    {
                        name: 'Number of Students',
                        values: Object.values(marks),
                    },
                ],
            },
            type: 'line',
            height: 250,
            
        });

        return () => {
            chart.destroy();
        };
    }, [data]);

    return <div ref={chartRef} className='card chart-flex'></div>;
};

export default LineChart;
